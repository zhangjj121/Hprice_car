from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import  ObjectDoesNotExist
from django.template.loader import render_to_string

from .models import *
import json
import datetime
import logging
# Create your views here.

from django.contrib.auth.hashers import make_password,check_password

def register(request):
    # if request.method == 'GET':
    #     return render(request,'register.html')
    #
    # elif request.methon == 'POST':
    #     user = UserInfo()
    #     uname = request.POST.get('uname')
    #     pwd = request.POST.get('password')
    #     spwd = request.POST.get('spassword')
    #     # 判断两次密码是否相同
    #     # 判断用户名是否存在
    #     if uname and pwd and spwd :
    #         res = UserInfo.objects.filter(username__exact=uname)
    #         if uname  in res:
    #             return redirect('/useinfo/ingister')
    #         else:
    #             user.username = uname
    #
    #             if pwd !=spwd:
    #                 return redirect('/useinfo/ingister')
    #                 user.password = pwd
    #                 user.save()
    #             return render(request,)

    if request.method =='POST':
        new_user = UserInfo()
        new_user.username = request.POST.get('new_user','')
        if new_user.username:
            return render(request,'register.html',{'msg':'用户不能为空'})
        olduser = UserInfo.objects.filter(username=new_user.username)
        if olduser:
            return render(request, 'register.html', {'msg': '用户已存在'})
        if request.POST.get('pwd') !=request.POST.get('spwd'):
            return render(request, 'register.html', {'msg': '密码前后不一致'})
        new_user.password = make_password(request.POST.get('pwd'),None,'pbkdf2_sha1')
        new_user.save()
        return render(request,'register.html')


    elif request.method =='GET':
        return render(request,'register.html')



def get_pdf(request):
    qr = 'hello'
    html = render_to_string('register.html',{'qr':qr})
    response = HttpResponse