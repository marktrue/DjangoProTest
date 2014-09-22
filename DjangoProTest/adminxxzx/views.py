#coding=utf-8
from django.http import HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views.generic import TemplateView

class AdminView:

    def __init__(self):
        return None

    def logon(self, request):
        if request.method == "GET":
            return HttpResponse('')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        return HttpResponseRedirect('/adminxxzx/')
    
    def index(self, request):
        if not request.user.is_authenticated():
            t = get_template('adminxxzx/logon.html')
            c = Context({'title':'用户登录'})
            c.update(csrf(request))
            html = t.render(c)
            return HttpResponse(html)
        t = get_template('adminxxzx/index.html')
        c = Context({'title':'用户登录'})
        html = t.render(c)
        return HttpResponse(html)

    def addArticle(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/adminxxzx/')
        if request.method == "GET":
            t = get_template("adminxxzx/newArticle.html")
            c = Context({'title':'用户登录'})
            html = t.render(c)
            return HttpResponse(html)
        elif request.method == "POST":
            return HttpResponse('')

    def getmenu(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('')
        #

    def notfound(self, request):
        return HttpResponseNotFound('404 别找了')

class AdminxxzxView(TemplateView):
    template_name = "adminxxzx/index.html"