from django.shortcuts import render, HttpResponse
from niexy.models import Test


# Create your views here.
def nxytestdb(request):
    nt = Test(name='聂暄玉')
    nt.save()
    return HttpResponse('<p>数据添加成功。byzys-nxy</p>')
