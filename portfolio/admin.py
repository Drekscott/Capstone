from django.contrib import admin

from .models import Client, Medium, Project
# Register your models here.
admin.site.register(Client)
admin.site.register(Medium)
admin.site.register(Project)
