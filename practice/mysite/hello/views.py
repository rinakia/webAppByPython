
from django.http.response import HttpResponse
from django.shortcuts import render # 19/07/25 追加
from . import forms # 19/08/02 追加
import datetime # 19/08/10 追加
import os # 19/08/13 追加

import base64 # 19/08/11 追加

import sys
sys.path.append("../users")
from users.models import User # 19/08/05 追加

def hello_world(request):
    return HttpResponse('Hello World!')

def hello_entry(request):
    # return render(request, 'login.html')
    return render(request, 'home.html')

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
    fileSumMax=100;
    isfile = os.path.isfile
    join = os.path.join
    foldername = 'save/memo/'
    number_of_files = sum(1 for item in os.listdir(foldername) if isfile(join(foldername, item)))
    print(number_of_files)
    dt_now = datetime.datetime.now()
    date_str = str(dt_now.year%100).zfill(2)+str(dt_now.month).zfill(2)+str(dt_now.day).zfill(2)
    filename =  foldername + request.GET.get("filename") + '_' + date_str +'.txt'
    memo = request.GET.get("memo")
    try:
        if number_of_files > fileSumMax:
            raise FileOverError("File more than" + str(fileSumMax))
        file = open(filename, 'w')
        file.write(memo)
        file.close()
        return render(request, 'memoDone.html')
    except IOError:
        d = {
        'message': '出力失敗',
        }
        return render(request, 'memo.html', d)
    except FileOverError:
        d = {
        'message': 'ファイル数が'+ str(fileSumMax) + 'を超えています',
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
    # import 
    # return render(request, 'handwritingRecogEntry.html')
    return render(request, 'handwritingRecogEntry_Sub.html')

def hello_handwritingRecogExecute(request):
    nameCanvas = request.GET.get("nameCanvas")
    if not nameCanvas:
        d = {
            'message' : "名前がありません",
        }
        return render(request, 'handwritingRecogEntry.html', d)
    else:
        canvas  = request.GET.get("canvas")
        # dec_data = base64.b64decode( enc_data.split(',')[1] )
        if not canvas:
            d = {
                'img': "",# 19/08/11 追加
                'message': "canvasの値が取れてないお",
                }
        else:
            d = {
                'img': canvas,# 19/08/11 追加
                'message': "",
                }
        return render(request, 'handwritingRecogEntry.html', d)
    
def hello_handwritingRecogExecute_Sub(request):
    numSum = 3; # selectboxの数
    
    import random
    rand = random.randint(1,10)
    num = request.GET.get("num")
    d = {
                'array' : ["abc", "efg"],
                'img' : "mlimg/digit_"+num+"_"+str(rand)+".png",
            }
    return render(request, 'handwritingRecogEntry_Sub.html', d)

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

