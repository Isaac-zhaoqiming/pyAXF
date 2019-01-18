from django.db import models

# Create your models here.
class BaseModel(models.Model):
    trackid = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=256)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        abstract = True

class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'

class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'

class MustBuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


class MainShow(BaseModel):
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=256)
    img1 = models.CharField(max_length=256)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=32)
    longname1 = models.CharField(max_length=200)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=200)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=200)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'

class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=40)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=10)
    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=200)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
    username = models.CharField(max_length=60,unique=True)
    password = models.CharField(max_length=60)
    portrait = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    rank = models.CharField(max_length=20,null=True)
    # True表示男,false表示女
    sex = models.NullBooleanField(default=True,null=True)
    isdeleted = models.NullBooleanField(default=False,null=True)

    class Meta:
        db_table = 'axf_user'

class Cart(models.Model):
    goods = models.ForeignKey(Goods)
    user = models.ForeignKey(User)
    num = models.IntegerField(default=0)
    is_selected = models.IntegerField(default=0)
    class Meta:
        db_table = 'axf_cart'

class OrderModel(models.Model):
    orderno = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    createtime = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'axf_order'

class OrderGoods(models.Model):
    order = models.ForeignKey(OrderModel,default=None)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_ordergoods'