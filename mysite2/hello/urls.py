#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
    url(r'^template/$', views.hello_template, name='hello_template'),  # 追加する
]

