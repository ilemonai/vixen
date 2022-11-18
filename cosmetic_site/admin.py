from django.contrib import admin

# Register your models here.
from .models import Topic, Appointment, Payment
admin.site.register(Topic)
admin.site.register(Appointment)
admin.site.register(Payment)