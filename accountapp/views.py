from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello World!') # alt+enter -> 파이참이 스스로 모듈 불러옴
