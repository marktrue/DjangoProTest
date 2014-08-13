#coding=utf-8
from django.http import HttpResponse
from django.http.response import HttpResponseNotFound
from mainview.models import Article
from django.template.loader import get_template
from django.template import Context
# MainView
class MainView:
    def __init__(self):
        return None

    def index(self, request):
        t = get_template('mainview/index.html')
        c = Context({'title':'测试'})
        html = t.render(c)
        return HttpResponse(html)

    #list all
    def list(self, request, col_id):
        t = get_template('mainview/list.html')
        a = Article.collectArticleByColId(col_id)
        #for p in a:
        #    print p.Title
        c = Context({'title':'测试'})
        html = t.render(c)
        return HttpResponse(html)
        #return HttpResponse('hello world' + str(col_id) + a[0].Title)
        #return None

    #show detail
    def show(self, request, atc_id):
        t = get_template('mainview/show.html')
        c = Context({'title':'测试'})
        html = t.render(c)
        return HttpResponse(html)

    def notfound(self, request):
        return HttpResponseNotFound('404 了骚年')