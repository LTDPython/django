#--coding=utf8--

#from __future__ import unicode_literals

from django.db import models

# Create your models here.
#创建一个名为tb_user的表

class tb_user(models.Model):
#(fields.W122) 'max_length' is ignored when used with IntegerField
#   user_id = models.BigIntegerField(max_length=20,null=None,primary_key=True,unique=True)
    user_id = models.BigIntegerField(null=None,primary_key=True,auto_created=True)
    unionid = models.CharField('微信unionid',max_length=32,null=None)
    mobile = models.CharField('手机号',max_length=11,null=None,default='Null')
    password = models.CharField('用户密码',max_length=64,null=None,default='Null')
    pay_password = models.CharField('支付密码',max_length=32,default='Null')
    bank_card_num = models.BooleanField('绑定的银行卡数量',max_length=1,null=None,default=0)
    level = models.BooleanField('用户当前等级（阶段）',max_length=2,null=None,default=0)
    reg_ip = models.CharField('注册IP',max_length=80,null=None)
#'max_length' is ignored when used with IntegerField
    from_channel = models.SmallIntegerField('推广渠道',null=None,default=0)
    from_reg = models.BooleanField('注册来源；0为wap；1为android；2为ios',max_length=1,null=None,default=0)
#'max_length' is ignored when used with IntegerField
    from_activity = models.SmallIntegerField('活动，关联活动表',null=None,default=0)
    realname = models.CharField('真实姓名',max_length=20,null=True)
    nick = models.CharField('用户昵称',max_length=100,null=True)
    card_no = models.CharField('身份证号',max_length=18,null=True)
    is_auth = models.BooleanField('1 认证， 0未证',max_length=1,null=None,default=0)
    safety_status = models.BooleanField('用户登录安全状态；1需要授权；0反之',max_length=1,null=None,default=1)
#(fields.W122) 'max_length' is ignored when used with IntegerField
#   login_count = models.IntegerField(max_length=8,null=None,default='0')
    login_count = models.IntegerField(' 登录次数',null=None,default=0)
    login_time = models.IntegerField('登陆时间',null=None,default='Null')
    create_time = models.IntegerField('创建时间',null=None,default='Null')
    update_time = models.IntegerField('更新时间',null=True,default='Null')

