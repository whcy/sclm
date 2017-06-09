
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from PIL import Image
# from filer.fields.image import FilerImageField
# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     cover = FilerImageField(related_name="book_covers")
#     back = FilerImageField(related_name="book_backs")

class Pro_icon(models.Model):
    icon_name = models.CharField(max_length=50, verbose_name=u'产品图标')
    photo = models.ImageField(upload_to='photos', default='protemp.jpg')
    def __unicode__(self):
        return self.icon_name


