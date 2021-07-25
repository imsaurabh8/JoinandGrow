
from django.contrib import admin

# Register your models here.
from .models import HireeInfo,HireeSkills

admin.site.register(HireeSkills)
admin.site.register(HireeInfo)
