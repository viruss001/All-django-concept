from django.db import models

# Create your models here.
class username(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    #it will return fname in caseof queryset returned
    def __str__(self) -> str:
        return self.fname