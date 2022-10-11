from django.shortcuts import render
from .models import Appointment
from django.db.models import Q

def _get_appointment_for_user(user):
    #returns a query set of topics that the user can access
    q = Q(public=True)
    if user.is_authenticated:
        q = q | Q(public=False, owner = user)
    return Appointment.objects.filter(q)
# Create your views here.


def index(request):
    """The home page for cosmetic site."""
    return render(request, 'cosmetic_site/index.html')

def profile(request):
    """profile."""
    profiles = _get_appointment_for_user(request.user)
    context = {'profiles':profiles}
    return render(request, 'cosmetic_site/profile.html', context)

def payment(request):
    """The home page for cosmetic site."""
    return render(request, 'cosmetic_site/payment.html')   
    
def failed(request):
    """The home page for cosmetic site."""
    return render(request, 'cosmetic_site/failed.html')   