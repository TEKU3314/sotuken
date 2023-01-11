# Create your models here.
from django.db import models

class Image(models.Model):
    """単語モデル"""
    image = models.ImageField(upload_to='images',blank=True,null=True)

