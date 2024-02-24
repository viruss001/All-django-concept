from django.db import models

# Create your models here.
class Recipy(models.Model):
    rname = models.CharField(max_length=100)
    rdes = models.TextField()
    rphot=models.ImageField(upload_to="recipy_img")
    
