from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .basa import *



class PageThree(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)

    def post(self, request):
        login = request.POST.get("login")
        password = request.POST.get("password")
        users = autoriz(login, password)
        if not users:
            context = {
                "message": "Введен не правильный пароль или логин"
            }
            return render(request, 'login.html', context=context)
        else:
            request.session["id_user"] = users[0].id
            return HttpResponseRedirect('index.html')


class MainPage(View):
    def get(self, request):

        tasks = get_material(request.session["id_user"])
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context=context)


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


