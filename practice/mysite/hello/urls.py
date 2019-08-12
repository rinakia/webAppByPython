#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# from django.conf.urls import url
from django.urls import path
from . import views

"""
urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
]
"""

"""
urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
    url(r'^templates/$', views.hello_template, name='hello_template'),  # 追加する
]
"""

urlpatterns = [
    # path('', views.hello_template, name='hello_template'),
    path('', views.hello_entry, name='hello_entry'),
    # path(r'^$', views.hello_post_query, name='hello_post'),
    path(r'^link/$', views.hello_link, name='hello_link'),
    path(r'^login/$', views.hello_login, name='hello_login'),
    path(r'^login/guest/$', views.hello_login_guest, name='hello_login_guest'),
    path(r'^backMenu/$', views.hello_backMenu, name='hello_backMenu'), # 19/08/02 追加
    path(r'^forms/$', views.hello_forms, name='hello_forms'), # 19/08/02 追加
    path(r'^insertAccountEntry/$', views.hello_insertAccountEntry, name='hello_insertAccountEntry'), # 19/08/05 追加
    path(r'^memoEntry/$', views.hello_memoEntry, name='hello_memoEntry'), # 19/08/02 追加
    path(r'^memoExecute/$', views.hello_memoExecute, name='hello_memoExecute'), # 19/08/02 追加
    path(r'^subContentMenuEntry/$', views.hello_subContentEntry, name='hello_subContent'), # 19/08/02 追加
    path(r'^machineLearnMenu/$', views.hello_machineLearnEntry, name='hello_machineLearnEntry'), # 19/08/10 追加
    path(r'^handwritingRecogEntry/$', views.hello_handwritingRecogEntry, name='hello_handwritingRecogEntry'), # 19/08/10 追加
    path(r'^handwritingRecogExecute/$', views.hello_handwritingRecogExecute, name='hello_handwritingRecogExecute'), # 19/08/10 追加
]

