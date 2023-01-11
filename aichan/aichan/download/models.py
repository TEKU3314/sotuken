# Create your models here.
from django.db import models

class Image(models.Model):
    """単語モデル"""
    image = models.CharField(verbose_name='image',max_length=25)

