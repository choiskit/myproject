# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import salt.client
from .models import *
from django.contrib.auth.decorators import login_required


def action_tmp(string, host_list):
    re = {}
    sa = salt.client.LocalClient()
    for i in host_list:
        if string != 'reboot':
            re.update(sa.cmd(i,'cmd.run',['echo ' + string + ' > C:\operation.txt']))
        else:
            re.update(sa.cmd(i, 'cmd.run', ['shutdown -r -t 0']))
    return re

@login_required
def result(request):
    proname = ProgramInfo.objects.values_list('proname', flat=True)
    if request.method == 'POST':
        error = ''
        re = {}
        host_list =request.POST.getlist('hostname')
        if len(host_list):
            s = request.POST['operation'] + ' ' + request.POST['program']
            re = action_tmp(s, host_list)
            if not re:
                error = '检查失败,请检查服务器salt-minon进程是否正常'
        else:
            error = '请选择服务器再进行操作'
            # return HttpResponse(error)
            # return render(request, 'results.html', {'error': error})
            # return HttpResponse(host_list)
    return render(request, 'results.html',{'re': re,'proname': proname, 'error': error})
    # return render(request, 'results.html')

def test(request):
    return render(request,'test.html')