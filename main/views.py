from django.shortcuts import render
from django.http import HttpResponse,Http404
from main import models
# Create your views here.
def create_article(request):
    authors=models.Author.objects.all()
    d={'authors':authors}
    if(request.method=='POST'):
        article_data={
            'title':request.POST['title'],
            'content':request.POST['content'],
        }
        article=models.Article.objects.create(**article_data)
        author=models.Author.objects.get(pk=request.POST['author'])
        article.authors.set([author])
        d['success']=True
    return render(request,'main/create_article.html',d)

def article(request,pk):
    try:article=models.Article.objects.get(pk=pk)
    except:raise Http404
    d={'article':article}
    return render(request,'main/article.html',d)

def author(request,pk):
    try:author=models.Author.objects.get(pk=pk)
    except:raise Http404
    d={'author':author}
    return render(request,'main/author.html',d)


def index(request):
    n=len(models.Article.objects.all())
    latest_article=models.Article.objects.all()
    if(n>=5):latest_article=latest_article[n-5::][::-1]
    else:latest_article=latest_article[::-1]
    '''
    hum isko SQL se bhi kr skte the by using ORDER_BY clause
    latest_Article=models.Article.objects.all().order_by('-createdAT')[:5]
    yha minus sign isley lgaaya hai taaki descending order m aa jaaye.
    '''
    d={'length':n,
        'latest_article':latest_article}
    return render(request,'main/index.html',d)
