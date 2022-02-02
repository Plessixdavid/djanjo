from django.contrib import admin
from .models import Ideotype, Ideogramm

# Register your models here.
admin.site.register(Ideogramm)
admin.site.register(Ideotype)