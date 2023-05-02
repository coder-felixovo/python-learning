from django.conf.urls import re_path

from . import views, testdb

urlpatterns = [
    re_path('hello/', views.hello),
    re_path('login/', views.login),
    re_path('index/', views.index),
    re_path('test_insert/', testdb.test_insert),
    re_path('test_select/', testdb.test_select),
    re_path('test_update/', testdb.test_update),
    re_path('test_delete/', testdb.test_delete)
]
