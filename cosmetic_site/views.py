from django.shortcuts import render, redirect
from .models import Appointment
from django.db.models import Q
from .forms import CardForm

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
	'''Add a new client'''
	if request.method != 'POST':
		#no data submitted; create a blank form
		form = CardForm()
	else:
		#POST data submitted; process data
		form = CardForm(request.POST)
		if form.is_valid():
			new_card = form.save(commit = False)
			new_card.save()
			return redirect('cosmetic_site:success')
	#display a blank or invalid form
	context = {'form':form}
	return render(request, 'cosmetic_site/payment.html', context)
    
def success(request):
    """The home page for cosmetic site."""
    return render(request, 'cosmetic_site/success.html')   