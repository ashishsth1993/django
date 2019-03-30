from django.urls import path
from pages.views import homepage_view

app_name = 'pages'

urlpatterns = [
    path('', homepage_view, name='homepage_view'),
]
