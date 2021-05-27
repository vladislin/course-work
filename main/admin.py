from django.contrib import admin
from .models import *


# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['sc_name', 'sc_manager', 'sc_address', 'sc_site', 'sc_phone', 'sc_lat', 'sc_lon']
    list_display_links = ['sc_name']


admin.site.register(School, SchoolAdmin)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['un_name', 'un_manager', 'un_address', 'un_site', 'un_phone', 'un_lat', 'un_lon']
    list_display_links = ['un_name']


admin.site.register(University, UniversityAdmin)
