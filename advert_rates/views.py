import copy
import json
import time
from threading import Thread

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from multiprocessing import Process
from utils import search_requests
import logging

logger = logging.getLogger(__name__)
many_response = []
empty_frase = [0]


@method_decorator(csrf_exempt, name='post')
class AdvertRates(View):
    def get(self, request):
        return render(request, 'advert_rates/advert_rates.html')

    def post(self, request):
        req = request.POST.get('name')
        result = search_requests.func_search(message=req)
        return render(request, 'advert_rates/advert_rates.html',
                      context={'result': result['response'], 'queryType': result['queryType']})


class AdvertRatesApi(View):
    def get(self, request):
        req = request.GET.get('req')
        result = search_requests.func_search(message=req) if req else {}
        return JsonResponse(result)

    def post(self, request):
        req = request.POST.get('req')
        result = search_requests.func_search(message=req) if req else {}
        return JsonResponse(result)


@csrf_exempt
def list_response(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        keywords = data.get('keywords')

        start_time = time.time()
        logger.info('Len incoming request:', len(keywords))
        if keywords:
            i_keywords = []

            for num, is_kw in enumerate(keywords):
                pull_thr = []
                i_keywords.append(is_kw)
                if (num > 0 and (num + 1) % 1000 == 0) or ((num + 1) == len(keywords)):
                    for ax, keyw in enumerate(i_keywords):
                        # thg = Process(target=func_in_thread, args=(keyw,))

                        thg = Thread(target=func_in_thread,
                                     args=(keyw,),
                                     name=f'My_thr-{(num + 1) // 1000 if (num + 1) % 1000 == 0 else (num + 1) // 1000 + 1}.{ax + 1}',
                                     daemon=True)
                        pull_thr.append(thg)
                        thg.start()

                    for i_thr in pull_thr:
                        i_thr.join()
                    i_keywords.clear()

            is_response = copy.deepcopy(many_response)
            many_response.clear()

            logger.warning(f'Incoming: {len(keywords)} frase')
            logger.warning(f'Response: {len(is_response)} frase')
            logger.warning(f'Time to response: {int(time.time() - start_time)} sec')
            logger.warning(f'Empty frase: {empty_frase[0]}')
            empty_frase[0] = 0
            return JsonResponse({'response': is_response})
        else:
            return JsonResponse({'response': 'bad request keywords not found'})

    else:
        return HttpResponseBadRequest()


def func_in_thread(keyword):
    rsp = []
    try:
        result = search_requests.func_search(message=keyword) if keyword else {}
    except Exception:
        result = {'response': []}

    items = []
    for numer, elem in enumerate(result['response']):
        items.append({'product_id': elem['product_id'],
                      'cpm': elem['cpm'],
                      'subject_name': elem['subject']['name']})
        if numer == 9:
            break
    rsp.append({'keyword': keyword, 'items': items})
    many_response.extend(rsp)
    if len(rsp[0]['items']) == 0:
        empty_frase[0] += 1
    # print('Поток:', threading.current_thread().name, f'длина ответа: {len(rsp)}', 'фраза:', rsp[0]['keyword'], 'кол-во значений:', [len(i_rsp['items']) for i_rsp in rsp])
