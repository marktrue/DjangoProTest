from django.db import models
from adminxxzx.models import Users

# Create your models here.
class Column(models.Model):
    Id = models.AutoField(primary_key=True)
    Level = models.PositiveIntegerField()
    Name = models.CharField(max_length=128,unique=True)
    Parent = models.ForeignKey('self')

    def __unicode__(self):
        return str(self.Id)

class Title_Type(models.Model):
    Id = models.AutoField(primary_key=True)
    Color = models.CharField(max_length=16)
    Bold = models.BooleanField()

    def __unicode__(self):
        return str(self.Id)


class Article(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=256)
    Content = models.TextField()
    Date = models.DateTimeField(auto_now=True)
    Count = models.PositiveIntegerField()
    Col_id = models.ForeignKey(Column)
    Author = models.ForeignKey(Users)
    Link = models.CharField(max_length=256)
    Jump = models.BooleanField()
    Check = models.BooleanField()
    Title_type = models.ForeignKey(Title_Type)

    @staticmethod
    def addArticle(title,content,colid,athr,jmp,chk,link='#',Titype='0',cnt=0):
        atc = Article(Title=title, \
                      Content=content, \
                      Count=cnt, \
                      Col_id=colid, \
                      Author=athr, \
                      Link=link, \
                      Jump=jmp, \
                      Check=chk)
        atc.save()
        return atc
    
    @staticmethod
    def getArticleById(aid):
        atcs = Article.objects.filter(Id=aid)
        return atcs.all()
    
    @staticmethod
    def getArticlesByTitle(title, limits=5):
        atcs = Article.objects.filter(Title=title).order_by('-Date')[0:limits]
        return atcs.all()
    
    @staticmethod
    def collectArticleByColId(colid, limits=5):
        atcs = Article.objects.filter(Col_id=colid).order_by('-Date')[0:limits]
        return atcs.all()

    def __unicode__(self):
        return str(self.Id)
    