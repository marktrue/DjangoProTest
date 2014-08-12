#coding=utf-8
from django.http import HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

class AdminView:

    def __init__(self):
        return None

    @csrf_exempt
    def logon(self, request):
        if request.method == "GET":
            return HttpResponse('')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        return HttpResponseRedirect('/')
    
    @csrf_protect
    def index(self, request):
        if not request.user.is_authenticated():
            t = get_template('index.html')
            c = Context({'title':'用户登录'})
            html = t.render(c)
            return HttpResponse(html)
        return HttpResponse('')

    def notfound(self, request):
        return HttpResponseNotFound('404 别找了')