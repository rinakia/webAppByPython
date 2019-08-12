#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" ---------------------------------
 
   Hello WorldのHttpレスポンスを返す
   
   https://qiita.com/podhmo/items/b6385fde9e32bbb8d57b

 
    ----------------------------------
""" 
# -*- coding:utf-8 -*-
# hello.py

import sys
from django.conf.urls import url, patterns
from django.http import HttpResponse


def index(request):
    import random
    return HttpResponse('Hello World. random={}\n'.format(random.random()))


urlpatterns = patterns(
    "",
    url(r'^$', index),
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    from django.conf import settings

    settings.configure(
        ALLOWED_HOSTS=["*"],
        DEBUG=True,
        ROOT_URLCONF=__name__,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
        )
    )
    # using this via 'python server-example.py runserver'
    execute_from_command_line(sys.argv)

