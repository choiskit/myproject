# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class IDCInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'机房名称')
    address = models.CharField(max_length=100,verbose_name=u'机房位置',null=True,blank=True)
    phone = models.CharField(max_length=15,verbose_name=u'机房电话',null=True, blank=True)
    codeid = models.CharField(max_length=50, verbose_name=u'客户号',null=True, blank=True)

    class Meta:
        verbose_name = u'机房信息表'
        verbose_name_plural = verbose_name
        db_table = "idcinfo"


    def __unicode__(self):
        return self.name

class CabInfo(models.Model):
    cablocate = models.CharField(max_length=20,verbose_name=u'机柜位置')
    IDCid = models.ForeignKey('IDCInfo')

    class Meta:
        verbose_name = u'机柜信息表'
        verbose_name_plural = verbose_name
        db_table = "cabinfo"


    def __unicode__(self):
        return self.cablocate


class ServerInfo(models.Model):
    type = models.CharField(max_length=20,verbose_name=u'服务器型号')
    serial = models.CharField(max_length=50, verbose_name=u'序列号')
    ipaddr = models.CharField(max_length=20,verbose_name=u'服务器IP地址')
    IDCid = models.ForeignKey('IDCInfo')
    CabID = models.ForeignKey('CabInfo',null=True, blank=True)

    class Meta:
        verbose_name = u'服务器信息表'
        verbose_name_plural = verbose_name
        db_table = "serverinfo"

    def __unicode__(self):
        return self.ipaddr

class ProgramInfo(models.Model):
    proname = models.CharField(max_length=100, verbose_name=u'系统启动程序名')
    operate = models.CharField(max_length=100, verbose_name=u'显示在操作界面的名字-中文', null=True, blank=True)

    class Meta:
        verbose_name = u'启动程序信息表'
	verbose_name_plural = verbose_name
	db_table = "programinfo"

    def __unicode__(self):
        return self.proname

    
