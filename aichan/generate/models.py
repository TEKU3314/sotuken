from django.db import models

class Type(models.Model):
    """タイプモデル"""
    
    name = models.CharField(max_length=25)

class Word(models.Model):
    """単語モデル"""

    word = models.CharField(max_length=25)
    count = models.IntegerField(default=0)
    typeid = models.ForeignKey(Type,on_delete=models.PROTECT)

