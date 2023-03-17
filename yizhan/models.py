from django.db import models

# Create your models here.
class Yizhan(models.Model):
    NA_zh = models.TextField("Answer_zh")
    NQ_zh = models.TextField("Question_zh")
    NA_en = models.TextField("Answer_en")
    NQ_en = models.TextField("Question_en")
    NA_ru = models.TextField("Answer_ru")
    NQ_ru = models.TextField("Question_ru")

    class Meta:
        db_table = 'Yizhan'
        verbose_name = 'Yizhan'



class User(models.Model):
    username = models.CharField('用户名', max_length=50, default='', unique=True)
    email = models.EmailField('邮箱', null=True)
    firstname = models.CharField('名', max_length=50, default='',null=True)
    lasttname = models.CharField('姓', max_length=50, default='',null=True)
    password = models.CharField('密码', max_length=32)
    phone = models.CharField('手机号', max_length=20,null=True)
    addr1 = models.CharField('地址', max_length=50,null=True)
    addr2 = models.CharField('备用地址', max_length=50,null=True)
    city = models.CharField('城市', max_length=20,null=True)
    country = models.CharField('国家', max_length=50,null=True)
    state = models.CharField('州', max_length=50,null=True)
    zip = models.CharField('邮编', max_length=20,null=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'User'