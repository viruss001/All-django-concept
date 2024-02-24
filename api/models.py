from django.db import models

# Create your models here.
class Userid(models.Model):
    uid = models.CharField(max_length= 100)
    def __str__(self) -> str:
        return self.uid
class username(models.Model):
    userid= models.ForeignKey(Userid,null =True,blank=True, on_delete=models.CASCADE,related_name="userid")
    fname=models.CharField(max_length= 100)
    age = models.IntegerField()
