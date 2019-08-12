
from django.http.response import HttpResponse
from django.shortcuts import render # 19/07/25 追加
from . import forms # 19/08/02 追加
import datetime # 19/08/10 追加

import base64 # 19/08/11 追加

import sys
sys.path.append("../users")
from users.models import User # 19/08/05 追加

def hello_world(request):
    return HttpResponse('Hello World!')

def hello_entry(request):
    return render(request, 'login.html')

def hello_template(request):
    # 値の受け渡し
    hello_data = {
    'str': 'request',
    'num': range(10),
    }
    return render(request, 'index.html', hello_data)

def hello_link(request):
    return render(request, 'link.html')

def hello_post_query(request):
    hello_data = {
        'name': request.POST.post('name')
    }
    return render(request, 'index.html', hello_data)

def hello_login(request):
    user_id = request.GET.get("user_id")
    password = request.GET.get("password")
    if user_id == 'user1' and password == 'pass1' :
        user = {
            'user_id': user_id,
            'password': password,
        }
        return render(request, 'menu.html', user)
    else:
        
        d = {
        'message': 'ログイン失敗',
        }
        return render(request, 'login.html', d)

def hello_login_guest(request):
    user = {
        'user_id': 'GUEST',
        'password': '',
    }
    return render(request, 'menu.html', user)

def hello_backMenu(request):
    return render(request, 'menu.html')

def hello_insertAccountEntry(request):
    form = forms.HelloForm(request.POST or None)
    if form.is_valid():
        User.objects.create(**form.cleaned_data)
        return redirect('hello:hello_insertAccountEntry')
    d = {
        'form': form,
        'hello_user': User.objects.all().order_by('-id')
    }
    return render(request, 'insertAccountEntry.html', d)

def hello_memoEntry(request):
    return render(request, 'memo.html')

def hello_memoExecute(request):
    dt_now = datetime.datetime.now()
    date_str = str(dt_now.year%100).zfill(2)+str(dt_now.month).zfill(2)+str(dt_now.day).zfill(2)
    filename = 'save/memo/' + request.GET.get("filename") + '_' + date_str +'.txt'
    memo = request.GET.get("memo")
    try:
        file = open(filename, 'w')
        file.write(memo)
        file.close()
        return render(request, 'memoDone.html')
    except IOError:
        d = {
        'message': '出力失敗',
        }
        return render(request, 'memo.html', d)
    else:
        d = {
        'message': '出力失敗',
        }
        return render(request, 'memo.html', d)
    
def hello_machineLearnEntry(request):
    return render(request, 'machineLearnMenu.html')

def hello_handwritingRecogEntry(request):
    return render(request, 'handwritingRecogEntry.html')

def hello_handwritingRecogExecute(request):
    nameCanvas = request.GET.get("nameCanvas")
    if not nameCanvas:
        d = {
            'message' : "名前がありません",
        }
        return render(request, 'handwritingRecogEntry.html', d)
    else:
        enc_data  = request.GET.get("canvas")
        # dec_data = base64.b64decode( enc_data.split(',')[1] )
        d = {
            'img': enc_data,# 19/08/11 追加
            'message': "",
        }
        return render(request, 'handwritingRecogEntry.html', d)

def hello_subContentEntry(request):
    return render(request, 'subContentMenu.html')

def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'forms.html', d)

