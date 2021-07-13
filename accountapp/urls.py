from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp' # 라우팅을 편하게 만들어주는 앱네임

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),

    path('create/', AccountCreateView.as_view(), name='create')
]
