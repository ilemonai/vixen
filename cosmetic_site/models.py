from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Appointment(models.Model):
    """the appointment for the client"""
    fullname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    procedure = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 200)
    initial_fund = models.CharField(max_length = 200)
    balance_fund = models.CharField(max_length = 200)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    public = models.BooleanField(default = 0)


    def __str__(self):
        '''Return the text representation of the model'''
        return self.fullname
