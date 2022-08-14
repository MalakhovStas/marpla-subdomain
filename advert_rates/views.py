from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from . import search_requests


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
