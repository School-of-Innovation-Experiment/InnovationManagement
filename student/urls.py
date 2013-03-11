# -*- coding: UTF-8 -*-
'''
Created on 2012-11-5

@author: tianwei
'''

from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from piston.resource import Resource
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',

    url(
        r'^$',
        direct_to_template, {'template': 'student/home.html'}
    ),
    url(
        r'^initial/$',
        direct_to_template, {'template': 'student/initial.html'}
    ),
    url(
        r'^midterm/$',
        direct_to_template, {'template': 'student/midterm.html'}
    ),
    url(
        r'^final/$',
        direct_to_template, {'template': 'student/final.html'}
    ),
    url(
        r'^progress/$',
        direct_to_template, {'template': 'student/progress.html'}
    ),
    url(
        r'^finance/$',
        direct_to_template, {'template': 'student/finance.html'}
    ),
)
