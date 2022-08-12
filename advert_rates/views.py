from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from . import search_requests


class AdvertRates(View):
    def get(self, request):
        return render(request, 'advert_rates/advert_rates.html')

    def post(self, request):
        req = request.POST.get('name')
        result = search_requests.func_search(message=req)
        if not result:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'advert_rates/advert_rates.html', context={'result': result})


class AdvertRatesApi(View):
    def get(self, request):
        print(request.GET)
        req = request.GET.get('req')
        result = search_requests.func_search(message=req) if req else {}
        return HttpResponse(str(result))

    def post(self, request):
        req = request.POST.get('req')
        result = search_requests.func_search(message=req) if req else {}
        return HttpResponse(str(result))
