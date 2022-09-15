from django.contrib import admin

# Register your models here.
from .models import Topic, Appointment
admin.site.register(Topic)
admin.site.register(Appointment)