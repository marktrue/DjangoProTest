#coding=utf-8
from django.http import HttpResponse
from django.http.response import HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

class AdminView:

    def __init__(self):
        return None

    @csrf_exempt
    def logon(self, request):
        return HttpResponse('')

    def index(self, request):
        return HttpResponse('')

    def notfound(self, request):
        return HttpResponseNotFound('404 别找了')