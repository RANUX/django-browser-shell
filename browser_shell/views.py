# -*- coding: UTF-8 -*-
import os
from django.shortcuts import render_to_response

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

def run(request):
    output = ''
    if request.method == 'POST':
        command = request.POST.get('command')
        output = os.popen(command).read()
    return render_to_response('browser_shell/run.html', {'output': output})