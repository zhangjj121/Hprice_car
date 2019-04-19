from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
ROLE_CHOICES=((0,'未激活') ,
(1,'激活')  )
SEX_CHOICES = ((0,'男'),(1,'女'))

BNNK_CHOICE=((0,'未绑定'),(1,'CBC'),(2,'ABC'),(3,'BC'),(4,'ICBC'))

class UserInfo(AbstractUser):
    role = models.IntegerField(verbose_name='角色',choices=ROLE_CHOICES,default=0)
    isActive = models.BooleanField(verbose_name='是否激活',default=True)
    isBen = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.username

class DetailInfo(models.Model):
    user = models.OneToOneField(UserInfo,verbose_name='用户')
    realname = models.CharField(max_length=50,null=False,verbose_name='真实姓名')
    age = models.IntegerField(verbose_name='年龄')
    ads = models.TextField(verbose_name='住址')
    identity = models.CharField(verbose_name='身份证号',max_length=18)
    sex = models.IntegerField(choices=SEX_CHOICES,default=0,verbose_name='性别')
    email = models.EmailField(verbose_name='邮箱')
    cellphone = models.CharField(max_length=20,null=False,verbose_name='电话')

    def __str__(self):
        return  self.user.username

    class Meta():

        verbose_name = '用户信息列表'
        verbose_name_plural='用户信息'

class Bank(models.Model):
    user=models.ForeignKey(UserInfo,verbose_name='用户')
    bankNo=models.CharField(verbose_name='卡号',max_length=50,null=False)
    bank=models.IntegerField(verbose_name='银行',choices=BNNK_CHOICE,default=0)
    bankpwd = models.CharField(verbose_name='交易密码',max_length=200,null=False)

    def __str__(self):
        return self.user.username

    class Meta():
        verbose_name_plural='银行信息'
        verbose_name='银行信息列表'


class Message(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    message =models.TextField(verbose_name='消息')
    datetime=models.DateTimeField(verbose_name='时间',auto_now_add=True)
    isRead = models.BooleanField(verbose_name='是否阅读',default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='消息记录列表'
        verbose_name_plural='消息列表'
