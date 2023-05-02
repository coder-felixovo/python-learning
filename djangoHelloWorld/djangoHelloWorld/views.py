import datetime

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Django hello world !")

def login(request):
    return render(request, 'login.html')

def index(request):
    context = {}
    context['title'] = '首页'
    context['list'] = ['Python', 'Java', 'C++']
    context['dict'] = {'name': 'Python', 'slogan': '人生苦短，我用Python'}
    context['greet'] = 'HELLO PYTHON'
    context['default_value'] = 0
    context['file_size'] = 2548
    context['a_date'] = datetime.datetime.now()
    context['str_limit'] = '这是一段文本abcdefg'
    context['to_baidu'] = '<a href="http://localhost:8080/index">跳转到项目首页</a>'
    context['score'] = 59
    context['abc_list'] = ['a', 'b', 'c', 'd', 'e', 'f']
    context['empty_list'] = []
    return render(request, 'index.html', context)
