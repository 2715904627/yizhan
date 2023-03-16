from django.http import HttpResponse
from django.shortcuts import render


def page_1_view(request):
    html = "<h1>This is the 1st page <h1>"
    return HttpResponse(html)

def page_2_view(request):
    html = "<h1>This is the 2nd page <h1>"
    return HttpResponse(html)


def index_page(request):
    html = "<h1>This is the index page <h1>"
    return HttpResponse(html)


def test_html(request):
    dic = {'username':'guoxiaonao','age':18}
    return render(request,'login.html',dic)

def static_html(request):
    return render(request, 'test_static.html')