import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from utils import search_requests


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

    # @method_decorator(csrf_exempt)
    def post(self, request):
        req = request.POST.get('req')
        result = search_requests.func_search(message=req) if req else {}
        return JsonResponse(result)


@csrf_exempt
def list_response(request, *args, **kwargs):
    if request.method == 'POST':
        # keywords = request.POST.get('keywords').split(', ')
        data = json.loads(request.body.decode())
        # print(data)
        keywords = data.get('keywords')
        # print(keywords, type(keywords))
        if keywords:
            response = []
            for keyword in keywords:
                result = search_requests.func_search(message=keyword) if keyword else {}
                items = []
                for elem in result['response']:
                    items.append({'product_id': elem['product_id'],
                                  'cpm': elem['cpm'],
                                  'subject_name': elem['subject']['name']})
                response.append({'keyword': keyword, 'items': items})
            return JsonResponse({'response': response})
        else:
            return JsonResponse({'response': 'bad request keywords not found'})

    else:
        return HttpResponseBadRequest()

# curl -d 'keywords=телефон, медведь'  http://127.0.0.1:8000/api/list/
# curl -X POST --header "Content-Type: application/json" --data '{"keywords": ["телефон", "медведь"]}'  http://127.0.0.1:8000/api/list/
