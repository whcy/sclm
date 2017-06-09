from __future__ import unicode_literals
from filer.models.foldermodels import Folder

from django.db import models
from filer.models.foldermodels import Folder
from filer.models.imagemodels import Image, 
# Create your models here.

class FolderProfile(models.Model):
    folder = models.OneToOneField(Folder)
    thum_img = 
