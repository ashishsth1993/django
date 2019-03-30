from django.shortcuts import render
from .models import LandingPage
from .models import AboutPage
from .models import ContactPage

from .forms import LandingForm


def homepage_create_view(request, *args, **kwargs):
    form = LandingForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'formbased/home_create.html', context)


def homepage_view(request, *args, **kwargs):
    landing_page = LandingPage.objects.get(id=1)
    about_page = AboutPage.objects.get(id=1)
    contact_page = ContactPage.objects.get(id=1)
    context = {
        'landing': landing_page,
        'about': about_page,
        'contact': contact_page,
    }
    return render(request, 'pages/home.html', context)