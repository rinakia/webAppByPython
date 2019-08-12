{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'BASE_DIR' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-7bb288a13222>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m         \u001b[0;34m'BACKEND'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m'django.template.backends.django.DjangoTemplates'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         'DIRS': [\n\u001b[0;32m----> 6\u001b[0;31m             \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBASE_DIR\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'templates'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m         ],\n\u001b[1;32m      8\u001b[0m         \u001b[0;34m'APP_DIRS'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'BASE_DIR' is not defined"
     ]
    }
   ],
   "source": [
    "TEMPLATES = [\n",
    "    {\n",
    "        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n",
    "        'DIRS': [\n",
    "            os.path.join(BASE_DIR, 'templates'),\n",
    "        ],\n",
    "        'APP_DIRS': True,\n",
    "        'OPTIONS': {\n",
    "            'context_processors': [\n",
    "                'django.template.context_processors.debug',\n",
    "                'django.template.context_processors.request',\n",
    "                'django.contrib.auth.context_processors.auth',\n",
    "                'django.contrib.messages.context_processors.messages',\n",
    "            ],\n",
    "        },\n",
    "    },\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
