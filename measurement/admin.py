from django.contrib import admin
from .models import Datchik, Temp

@admin.register(Datchik)
class DatchikAdmin(admin.ModelAdmin):
    pass

@admin.register(Temp)
class TempAdmin(admin.ModelAdmin):
    pass


# Register your models here.
