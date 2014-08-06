#coding=gb2312
from django.http import HttpResponse
from mainview.models import Article
from django.template.loader import get_template
from django.template import Context
# MainView
class MainView:
    def __init__(self):
        return None

    def index(self, request):
        t = get_template('index.html')
        c = Context({'title':'测试'})
        html = t.render(c)
        return HttpResponse(html)

    #list all
    def list(self, request, col_id):
        a = Article.collectArticleByColId(col_id)
        #for p in a:
        #    print p.Title
        return HttpResponse('hello world' + str(col_id) + a[0].Title)
        #return None

    #show detail
    def show(self, request, *args):
        return None