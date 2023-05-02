from django.conf.urls import re_path

from . import views

urlpatterns = [
    re_path('hello/', views.hello),
    re_path('login/', views.login),
    re_path('index/', views.index)
]
