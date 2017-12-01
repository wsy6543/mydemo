from django.db import models
class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField()

    class Meta:
        db_table = "goods"  # 更改表名
    def info(self):
        return {'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'typeid':self.typeid}


#用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.IntegerField()

    class Meta:
        db_table = "users"  # 更改表名
    def info(self):
        return {'id':self.id,'username':self.username,'address':self.address,'code':self.code,'phone':self.phone,'name':self.name}

#商品类别信息模型
class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    class Meta:
        db_table = "type"  # 更改表名
    def info(self):
        return {'pid':self.pid,'name':self.name,'id':self.id}

class Detail(models.Model):
    orderid = models.TextField()
    goodid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()
    class Meta:
        db_table = "detail"


class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    total = models.FloatField()

    class Meta:
        db_table = "orders"