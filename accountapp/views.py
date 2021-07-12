from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        return render(request, 'accoutapp/hello_world.html',
                      context={'text': temp})
    else:
        return render(request, 'accoutapp/hello_world.html',
                      context={'text': 'GET METHOD!'})

