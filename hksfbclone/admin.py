from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.item)
admin.site.register(models.comment)
admin.site.register(models.likes)
admin.site.register(models.profile_details)


