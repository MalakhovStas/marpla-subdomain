from typing import Dict
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .my_utils import search_requests
from django.shortcuts import render


# class AdvertRates(TemplateView):
#     template_name = 'advert_rates/advert_rates.html'
#
#     def get_context_data(self, **kwargs) -> Dict:
#         context = super().get_context_data(**kwargs)
#         context['text'] = search_requests.func_search('штаны')
#         return context

class AdvertRates(View):
    def get(self, request):
        return render(request, 'advert_rates/advert_rates.html')

    def post(self, request):
        result = search_requests.func_search(request.POST.get('name'))
        if not result:
            result = 'по вашему запросу ничего не найдено'
            return HttpResponseRedirect('/')
        else:
            return render(request, 'advert_rates/advert_rates.html', context={'text': result})
