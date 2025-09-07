from django.db import models

# Create your models here.

class user(models.Model):
    id= models.AutoField(primary_key=True)
    full_name=models.CharField(verbose_name="ism-familya",max_length=100)
    username=models.CharField(verbose_name="telegram username",max_length=100,null=True)
    telegram_id=models.BigIntegerField(verbose_name="telegram ID",unique=True,default=1)
    locatsiya_lat=models.BigIntegerField(verbose_name="loc. latude",null=True)
    locatsiya_long=models.BigIntegerField(verbose_name="loc. langtude",null=True)
    number=models.BigIntegerField(verbose_name="telefon raqam")

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"