from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View

from . import search_requests


class AdvertRates(View):
    def get(self, request):
        return render(request, 'advert_rates/advert_rates.html')

    def post(self, request):
        result = search_requests.func_search(request.POST.get('name'))
        if not result:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'advert_rates/advert_rates.html', context={'result': result})


class AdvertRatesJson(View):
    def get(self, request):
        print(request.GET)
        name = request.GET.get('req')
        result = search_requests.func_search(name) if name else {}
        return JsonResponse(result)

    def post(self, request):
        name = request.POST.get('req')
        result = search_requests.func_search(name) if name else {}
        return JsonResponse(result)
