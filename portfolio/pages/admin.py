from django.contrib import admin
from pages.models import LandingPage, AboutPage, ContactPage


admin.site.register(LandingPage)
admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.site_header = 'Codewithashish'