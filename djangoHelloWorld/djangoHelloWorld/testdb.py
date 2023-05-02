from django.http import HttpResponse
from djangoHelloModel.models import Person


# 数据库操作
def test_insert(request):
    person = Person(name='Amy')
    person.save()
    return HttpResponse("<p>数据添加成功</p>")

def test_select(request):
    response = ""

    list = Person.objects.all()

    for item in list:
        response += item.name + " "

    return HttpResponse("<p>" + response + "</p>")

def test_update(request):
    person = Person.objects.get(id=1)
    person.name = person.name + "-update"
    person.save()
    return HttpResponse("<p>修改数据成功</p>")

def test_delete(request):
    person = Person.objects.get(id=1)
    person.delete()
    return HttpResponse("<p>删除数据成功</p>")