from django.contrib import admin
from .models import Part
# Register your models here.


class AdminPart(admin.ModelAdmin):
    list_display = ('name', 'id_name', 'parttype', 'pic')

admin.site.register(Part, AdminPart)
