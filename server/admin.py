# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
from django.http import HttpResponse
import salt.client
from django.shortcuts import render


@admin.register(IDCInfo)
class IdcInfoAdmin(admin.ModelAdmin):
    list_display = ['name','phone']


@admin.register(CabInfo)
class CabInfoAdmin(admin.ModelAdmin):
   list_display = ['cablocate']


def action_tmp(string, queryset):
    re = []
    sa = salt.client.LocalClient()
    for i in queryset.values_list('ipaddr', flat=True):
        if string != 'reboot':
            re.append(sa.cmd(i,'cmd.run',['echo ' + string + ' > C:\operation.txt']))
        else:
	    re.append(sa.cmd(i, 'cmd.run', ['shutdown -r -t 0']))
    return re

def reboot(modeladmin, request, queryset):
    re = action_tmp('reboot', queryset)
    return HttpResponse(re)

# def start_ra(modeladmin,request,queryset):
#     re = action_tmp('start program ra', queryset)
#     return HttpResponse(re)
# start_ra.short_description = u"启动RA"
#
# def start_QuoteDataAdmin(modeladmin,request,queryset):
#     re = action_tmp('restart program QuoteDataAdmin', queryset)
#     return HttpResponse(re)
#
# def stop_QuoteDataAdmin(modeladmin,request,queryset):
#     re = action_tmp('stop program QuoteDataAdmin', queryset)
#     return HttpResponse(re)
#
# def start_TBDataRefiner(modeladmin,request,queryset):
#     re = action_tmp('restart program TBDataRefiner', queryset)
#     return HttpResponse(re)
#
# def stop_TBDataRefiner(modeladmin,request,queryset):
#     re = action_tmp('stop program TBDataRefiner', queryset)
#     return HttpResponse(re)
#
# def start_ReceivePluginLoader(modeladmin,request,queryset):
#     re = action_tmp('restart program ReceivePluginLoader', queryset)
#     return HttpResponse(re)
#
# def stop_ReceivePluginLoader(modeladmin,request,queryset):
#     re = action_tmp('stop program ReceivePluginLoader', queryset)
#     return HttpResponse(re)
#
#
# def start_Glacier(modeladmin,request,queryset):
#     re = action_tmp('restart program Glacier', queryset)
#     return HttpResponse(re)
#
# def stop_Glacier(modeladmin,request,queryset):
#     re = action_tmp('stop program Glacier', queryset)
#     return HttpResponse(re)
#
# def start_all(modeladmin,request,queryset):
#     re = action_tmp('restart program all', queryset)
#     return HttpResponse(re)
#
# def stop_all(modeladmin,request,queryset):
#     re = action_tmp('stop program all', queryset)
#     return HttpResponse(re)


# def test(modeladmin,request,queryset):
#     return render(request, 'results.html', { 'queryset': queryset} )
def check(queryset,check_str):
    re = {}
    error = ''
    li = queryset.values_list('ipaddr', flat=True)
    sa = salt.client.LocalClient()
    for i in li:
        re.update(sa.cmd(i, 'checklog.' + check_str))
    error_ms = '检查失败,请检查服务器salt-minon进程是否正常'
    if not re:
        error = error_ms
    return  re,error

proname = ProgramInfo.objects.values_list('proname', flat=True)
def RemoveTodayToHis(modeladmin, request, queryset):
    re,error = check(queryset,'RemoveTodayToHis')
    # re = {}
    # li = queryset.values_list('ipaddr', flat=True)
    # sa = salt.client.LocalClient()
    # for i in li:
    #     re.update(sa.cmd(i,'checklog.RemoveTodayToHis'))
    # error = ''
    # if not re :
    #     error = '检查失败,请检查服务器salt-minon进程是否正常'
    return render(request, 'results.html', { 're': re, 'proname': proname, 'error': error })
#    return HttpResponse(re.values())

def Summary(modeladmin,request,queryset):
    re, error = check(queryset, 'Summary')
    return render(request, 'results.html', { 're': re, 'proname': proname, 'error': error })

def Control(modeladmin, request, queryset):
    li = queryset.values_list('ipaddr',flat=True)
    return render(request, 'results.html', {'li': li, 'proname': proname})

Control.short_description = u'操作界面'
RemoveTodayToHis.short_description = u'检查数据迁移'
reboot.short_description = u'重启操作系统'
Summary.short_description = u'检查日出日结'
# start_QuoteDataAdmin.short_description = u"启动,重启QuoteDataAdmin"
# stop_QuoteDataAdmin.short_description = u"关闭QuoteDataAdmin"
# start_TBDataRefiner.short_description = u"启动TBDataRefiner"
# stop_TBDataRefiner.short_description = u"关闭TBDataRefiner"
# start_ReceivePluginLoader.short_description = u"启动,重启ReceivePluginLoader"
# stop_ReceivePluginLoader.short_description = u"关闭ReceivePluginLoader"
# start_Glacier.short_description = u"启动,重启Glacier"
# stop_Glacier.short_description = u"关闭Glacier"
# start_all.short_description = u"启动,重启所有程序"
# stop_all.short_description = u"关闭所有程序"
#def start_ra(modeladmin,request,queryset):
#    re = []
#    sa = salt.client.LocalClient()
#    for i in queryset.values_list('ipaddr', flat=True):
#        re.append(local.cmd(i, 'cmd.run', ['echo ra > D:\operation.txt']))
#    return HttpResponse(re)



@admin.register(ProgramInfo)
class ProgramInfoAdmin(admin.ModelAdmin):
    list_display = ['proname', 'operate']

@admin.register(ServerInfo)
class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ['ipaddr', 'IDCid']
    actions = [ Summary, RemoveTodayToHis, reboot, Control ]

admin.site.site_header = 'tradeblazer'
