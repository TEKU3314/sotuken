from django.db import models

class Type(models.Model):
    """タイプモデル"""
    name = models.CharField(max_length=25)

class BackGroundWord(models.Model):
    """背景画モデル"""
    word = models.CharField(max_length=50)
    word_en = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    typeid = models.ForeignKey(Type,on_delete=models.PROTECT)

class GirlWord(models.Model):
    """女の子モデル"""
    word = models.CharField(max_length=50)
    word_en = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    typeid = models.ForeignKey(Type,on_delete=models.PROTECT)

