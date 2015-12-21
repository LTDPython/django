#--coding=utf8--

#from __future__ import unicode_literals

from django.db import models

# Create your models here.
#创建一个名为tb_user的表

class tb_user(models.Model):
    user_id = models.BigIntegerField(max_length=20,null=None,primary_key=True,unique=True)
    open_id = models.CharField(max_length=32,null=True)
    mobile = models.CharField(max_length=11,null=None,default='Null')
    password = models.CharField(max_length=64,null=None,default='Null')
    reg_ip = models.CharField(max_length=80,null=None)
    realname = models.CharField(max_length=20,null=True)
    nick = models.CharField(max_length=100,null=True)
    card_no = models.CharField(max_length=18,null=True)
    is_auth = models.BooleanField(max_length=1,null=None,default='0')
    login_count = models.IntegerField(max_length=8,null=None,default='0')
    login_time = models.IntegerField(max_length=10,null=None,default='Null')
    create_time = models.IntegerField(max_length=10,null=None,default='Null')
    update_time = models.IntegerField(max_length=10,null=True,default='Null')
