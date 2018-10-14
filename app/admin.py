from django.contrib import admin

# Register your models here.
from app.models import Equipments, Members, Users

admin.site.register(Equipments)

admin.site.register(Members)

admin.site.register(Users)