from django.db import models

# Create your models here.
class Yizhan(models.Model):
    NA_zh = models.TextField("Answer_zh")
    NQ_zh = models.TextField("Question_zh")
    NA_en = models.TextField("Answer_en")
    NQ_en = models.TextField("Question_en")
    NA_ru = models.TextField("Answer_ru")
    NQ_ru = models.TextField("Question_ru")