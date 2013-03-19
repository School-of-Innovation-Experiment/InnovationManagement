'''
Created on 2013-3-18

@author: sytmac
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
urlpatterns = patterns('',
    url(
        r'^expert_dispatch/$',
        direct_to_template, {'template': 'academicStaff/expert_dispatch.html'}
    ),
    url(
        r'^basic_info/$',
        direct_to_template, {'template': 'academicStaff/basic_info.html'}
    ),
    url(
        r'^teacher_dispatch/$',
        direct_to_template, {'template': 'academicStaff/teacher_dispatch.html'}
    ),
    url(
        r'^password_admin/$',
        direct_to_template, {'template': 'academicStaff/password_admin.html'}
    ),
    url(
        r'^subject_feedback/$',
        direct_to_template, {'template': 'academicStaff/subject_feedback.html'}
    ),
    url(
        r'^$',
        direct_to_template, {'template': 'academicStaff/administrator.html'}
    ),
    url(
        r'^settings$',
        direct_to_template, {'template': 'academicStaff/settings.html'}
    ),
)
