# from django.contrib.auth.models import AbstractUser
from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _


# 作成 19/08/02

"""
    カスタムユーザー データ定義クラス

    ユーザーの管理項目を増やしたい場合はここにフィールドを定義します。
    例：住所、電話番号など
    
"""
    
# class User(AbstractUser):
class User(models.Model):
    
    # id
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    """
    user_id = models.IntegerField(
        verbose_name='id',
    )
    """

    # first_name、last_nameの代わりにfull_nameを用意する
    name = models.CharField(
        verbose_name='name',
        max_length=100,
        # required=True,
    )
    
    # pass
    password = models.CharField(
        verbose_name='password',
        max_length=100,
        blank=True,
        # required=True,
    )
    
    # gender 
    #  性別を選択する選択肢を宣言
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )
    gender = models.IntegerField(
        verbose_name='gender',
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        # required=True,
    )
    
    # auth 権限(複数種類)
    auth = models.PositiveIntegerField(
        verbose_name = 'auth', 
    )
    
    # mail address
    mail = models.EmailField(
        verbose_name = 'mail',
        max_length=255, 
        blank=True, # 空でもおk
        # unique=True, # 一意
    )

    # スタッフ権限のデフォルトをTrueに変更する
    # ※ 原則ログインして利用することを想定している。

    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
    )

    # get_full_name()の変更
    """
    def get_name(self):
        if self.name:
            return self.name
        else:
            return self.name + '（no name）'
    """

    # 選択リストでの表示
    def __str__(self): # クラスを呼び出したときに何が帰るか
        return "<{0}>".format(self.name)

