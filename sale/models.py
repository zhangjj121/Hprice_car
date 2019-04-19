from django.db import models
from userinfo.models import UserInfo
# Create your models here.

EXAMINE_CHOICE = ((0,'审核中'),
                  (1,'审核通过'),
                  (2,'审核未通过'))
class Brand(models.Model):
    logo_brand = models.ImageField(verbose_name='标志',upload_to='image/logo',default='normal,png')
    btitle = models.CharField(verbose_name='名称',max_length=50,null=False)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)


    def __str__(self):
        return self.btitle


    class Meta:
        verbose_name_plural='汽车品牌'
        verbose_name ='汽车品牌列表'


class CarInfo(models.Model):
    brand= models.ForeignKey(Brand,verbose_name='品牌')
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    ctitle = models.CharField(verbose_name='车名',max_length=50,null=False)
    regist_date = models.DateField(verbose_name='上牌日期',null=False)
    engineNo = models.CharField(verbose_name='发动机号',max_length=50,null=False)
    mileage = models.IntegerField(verbose_name='公里数')
    maintenance = models.BooleanField(verbose_name='维修记录',default=False)
    price = models.DecimalField(verbose_name='价格',max_digits=8,decimal_places=2)
    extractprice = models.DecimalField(verbose_name='成交价格',max_digits=8,decimal_places=2)
    newprice=models.DecimalField(verbose_name='新车价格',max_digits=8,decimal_places=2)
    picture = models.ImageField(upload_to='image/car',default='normal.png',verbose_name='图片')
    formalities = models.BooleanField(verbose_name='手续',default= True)
    debt = models.BooleanField(verbose_name='债务',default=False)
    promise = models.TextField(verbose_name='承诺')
    examine = models.IntegerField(choices=EXAMINE_CHOICE,default=0,verbose_name='审核进度')
    isPurchase = models.BooleanField(verbose_name='是否购买',default=False)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return '{}-{}'.format(self.brand,self.ctitle)

    class Meta:
        verbose_name='汽车信息列表'
        verbose_name_plural='汽车信息'