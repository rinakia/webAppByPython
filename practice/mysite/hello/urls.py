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
    # path(r'^handwritingRecogEntry/$', views.hello_handwritingRecogEntry, name='hello_handwritingRecogEntry'), # 19/08/10 追加
    path(r'^handwritingRecogEntry/$', views.hello_handwritingRecogEntry, name='hello_handwritingRecogEntry'), # 19/08/10 追加
    path(r'^handwritingRecogExecute/$', views.hello_handwritingRecogExecute_Sub, name='hello_handwritingRecogExecute_Sub'), # 19/08/10 追加
    path(r'^handwritingRecogExecute/$', views.hello_handwritingRecogExecute, name='hello_handwritingRecogExecute'), # 19/08/10 追加
    #
    path(r'^usersApp/loginEntry/$', views.users_loginEntry, name='users_loginEntry'), # 19/08/22 追加
    path(r'^usersApp/loginExecute/$', views.users_loginExecute, name='users_loginExecute'), # 19/08/22 追加
    path(r'^usersApp/loginGuestExecute/$', views.users_loginGuestExecute, name='users_loginGuestExecute'), # 19/08/22 追加
    path(r'^usersApp/insertUserEntry/$', views.users_insertUserEntry, name='users_insertUserEntry'), # 19/08/22 追加
    path(r'^usersApp/insertUserExecute/$', views.users_insertUserExecute, name='users_insertUserExecute'), # 19/08/22 追加
    #
    path(r'^vbsApp/vbsMenu/$', views.vbs_menu, name='vbs_menu'), # 19/09/06 追加
    path(r'^vbsApp/vbsDownload/$', views.vbs_downloadEntry, name='vbs_downloadEntry'), # 19/09/06 追加
    path(r'^vbsApp/vbsUpload/$', views.vbs_uploadEntry, name='vbs_uploadEntry'), # 19/09/06 追加
]

