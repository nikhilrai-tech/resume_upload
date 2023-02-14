from django.contrib import admin
from . models import resume

@admin.register(resume)
class resumeadmin(admin.ModelAdmin):
    list_display=["id","name","dob","gender","address","city","pin","state","mob","loc","img","res"]