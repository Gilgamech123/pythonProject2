from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .basa import *
from django.http import HttpResponseRedirect


#class MainPage(View):
  #  def get(self, request):
   #     context = {}
    #    return render(request, '', context=context)

class FirstSecond(View):
    def get(self, request):
        date_today = timezone.now()
        info = get_material()
        context = {
            'date_today': date_today,
            'info': info
        }
        return render(request, 'index.html', context=context)

class PageSecond(View):
    def get(self, request):
        context = {}
        return render(request, 'index2.html', context=context)

class PageThree(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)