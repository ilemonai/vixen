from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for cosmetic site."""
    return render(request, 'cosmetic_site/index.html')

def profile(request):
    """profile."""
    return render(request, 'cosmetic_site/profile.html')