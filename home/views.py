from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(), name='dispatch')
class HomeView(View):
    def get(self, request):
        return HttpResponse('hello world')
