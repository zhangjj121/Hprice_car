from django.db import models
from userinfo.models import *
from sale.models import *
# Create your models here.

ORDER_STATUS=(
    (0,'未出价'),
    (1,'已出价'),
    (2,'订单关闭'),
)

class Cart(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    car = models.ForeignKey(CarInfo,verbose_name='车辆')
    brand = models.CharField(verbose_name='品牌',max_length=8,null=False)
    price = models.DecimalField(verbose_name='价格',max_digits=8,decimal_places=2)
    mileage = models.IntegerField(verbose_name='公里数')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name_plural='意愿列表'
        verbose_name='意愿出价表'


class Order(models.Model):
    buy_user = models.ForeignKey(UserInfo,verbose_name='买家',related_name='buser')
    sale_user = models.ForeignKey(UserInfo, verbose_name='卖家',related_name='suser')
    orderNo = models.CharField(max_length=50,verbose_name='订单号',null=False)
    brand = models.CharField(max_length=8,verbose_name='品牌',null=False)
    ctitle = models.CharField(max_length=50,verbose_name='车名',null=False)
    orderStatus = models.IntegerField(choices=ORDER_STATUS,default=0,verbose_name='订单状态')
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.buy_user.username

    class Meta:
        verbose_name='订单列表详情'
        verbose_name_plural='订单列表'