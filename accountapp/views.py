from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world')) # reverse 특정 앱 안에 특정 이름을 가진 라우트로 가라

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView): # from django.views.generic import CreateView
    model = User # ctrl + b 누르면 세부내용 볼 수 있다.
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # _lazy Hello_world의 reverse와 동일하나 함수에서 불러오느냐 클래스에서 불러오느냐의 차이
    template_name = 'accountapp/create.html'
# 로직 만들었으면 라우팅(urls.py)

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'





