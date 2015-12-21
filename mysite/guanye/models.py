#--coding=utf8--

#from __future__ import unicode_literals

from django.db import models

# Create your models here.
#创建一个名为tb_user的表

class tb_user(models.Model):
#(fields.W122) 'max_length' is ignored when used with IntegerField
#   user_id = models.BigIntegerField(max_length=20,null=None,primary_key=True,unique=True)
    user_id = models.BigIntegerField(null=None,primary_key=True,auto_created=True)
    unionid = models.CharField(max_length=32,null=None,verbose_name='微信unionid')
    mobile = models.CharField(max_length=11,null=None,default='Null',verbose_name='手机号')
    password = models.CharField(max_length=64,null=None,default='Null',verbose_name='用户密码')
    pay_password = models.CharField(max_length=32,default='Null',verbose_name='支付密码')
    bank_card_num = models.BooleanField(max_length=1,null=None,default=0,verbose_name='绑定的银行卡数量')
    level = models.BooleanField(max_length=2,null=None,default=0,verbose_name='用户当前等级（阶段）')
    reg_ip = models.CharField(max_length=80,null=None,verbose_name='注册IP')
#'max_length' is ignored when used with IntegerField
    from_channel = models.SmallIntegerField(null=None,default=0,verbose_name='推广渠道')
    from_reg = models.BooleanField(max_length=1,null=None,default=0,verbose_name='注册来源；0为wap；1为android；2为ios')
#'max_length' is ignored when used with IntegerField
    from_activity = models.SmallIntegerField(null=None,default=0,verbose_name='活动，关联活动表')
    realname = models.CharField(max_length=20,null=True,verbose_name='真实姓名')
    nick = models.CharField(max_length=100,null=True,verbose_name='用户昵称')
    card_no = models.CharField(max_length=18,null=True,verbose_name='身份证号')
    is_auth = models.BooleanField(max_length=1,null=None,default=0,verbose_name='1 认证， 0未证')
    safety_status = models.BooleanField(max_length=1,null=None,default=1,verbose_name='用户登录安全状态；1需要授权；0反之')
#(fields.W122) 'max_length' is ignored when used with IntegerField
#   login_count = models.IntegerField(max_length=8,null=None,default='0')
    login_count = models.IntegerField(null=None,default=0,verbose_name=' 登录次数')
    login_time = models.IntegerField(null=None,default='Null',verbose_name='登陆时间')
    create_time = models.IntegerField(null=None,default='Null',verbose_name='创建时间')
    update_time = models.IntegerField(null=True,default='Null',verbose_name='更新时间')

