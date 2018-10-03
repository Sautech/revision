from django.db import models

# Create your models here.
class Equipments(models.Model):
    status = models.BooleanField(default=False)
    item_image = models.ImageField(upload_to=f'profile',max_length = 250, unique =True)
    music = models.BooleanField(default=False)