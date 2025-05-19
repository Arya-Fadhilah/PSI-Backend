from django.contrib import admin
from .models import Patient, MCURecord

admin.site.register(Patient)
admin.site.register(MCURecord)