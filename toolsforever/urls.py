"""toolsforever URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from examenapp.views import home, contact, fabrieksoverzicht, createfabriek, deletefabriek, editfabriek

# Alle urls worden hier aangemaakt, met de aangegeven view die gebruikt gaat worden.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^contact/', contact, name='contact'),
    url(r'^toolsforever/overzicht/', fabrieksoverzicht.as_view(), name='fabrieksoverzicht'),
    url(r'^toolsforever/create/', createfabriek.as_view(), name='createfabriek'),
    url(r'^toolsforever/delete/(?P<pk>\d+)$', deletefabriek.as_view(), name='deletefabriek'),
    url(r'^toolsforever/edit/(?P<pk>\d+)$', editfabriek.as_view(), name='editfabriek'),
]
