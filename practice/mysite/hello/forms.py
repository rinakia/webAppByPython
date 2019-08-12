from django import forms

from .models import Item

# from ..users.models import User

import sys
sys.path.append("../users")
from users.models import User


class HelloForm(forms.ModelForm):
# class HelloForm(forms.Form):
    
    """
    モデルフォーム構成クラス
    ・公式 モデルからフォームを作成する
    https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/
    """
    
    """
    name = forms.CharField(
        label='name',
        max_length=20,
        required=True,
        widget=forms.TextInput(),
    )
    """
    
    
    class Meta:
        # model = Item
        model = User
        fields = ('name', 'gender')
        widgets = {
            # 'name': forms.TextInput(attrs={'size': 40}),
            # 'message': forms.Textarea(attrs={'cols': 80, 'rows': 20})
            'name': forms.TextInput(),
            'gender': forms.Select(),
        }

        # 以下のフィールド以外が入力フォームに表示される
        # AutoField
        # auto_now=True
        # auto_now_add=Ture
        # editable=False
        
        
        
        
    
        

