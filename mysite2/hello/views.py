#!/usr/bin/env python
# coding: utf-8


from django.http.response import HttpResponse
from django.shortcuts import render # 追加する

def hello_template(request):
    return render(request, 'index.html')

