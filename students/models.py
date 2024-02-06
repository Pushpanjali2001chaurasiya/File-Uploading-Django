from django.db import models

class registration(models.Model):
    name = models.CharField('name',max_length=50)
    docu = models.FileField(upload_to='images/', max_length=255)
    

