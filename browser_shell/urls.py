# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from views import run


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


urlpatterns = patterns('',
    url(r'^run/$', run, name='browser_shell_run')
)