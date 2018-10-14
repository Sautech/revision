from django.db import models

# Create your models here.
class Equipments(models.Model):
    status = models.BooleanField(default=False)
    item_image = models.ImageField(upload_to=f'profile',max_length = 250, unique =True)
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Members(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=50)
    member_pic=models.ImageField(upload_to=f'members',max_length=250,unique=True)

class Users(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=50)


