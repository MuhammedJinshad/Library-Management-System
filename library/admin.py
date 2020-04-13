from django.contrib import admin
from library import models
# Register your models here.

admin.site.register(models.Department)
admin.site.register(models.Cususer)
admin.site.register(models.Issuedbooks)
admin.site.register(models.IssuedHistorys)
admin.site.register(models.Book)
