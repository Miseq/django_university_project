"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset
from django.urls import path
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'places', views.PlaceViewSet)
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^konto/$', views.konto),
    url(r'^edycja_konta/', views.konto_edycja),
    url(r'^logowanie/', views.logowanie),
    url(r'^miejsca/', views.miejsca),
    url(r'^miejsce_dodaj/', views.miejsce_dodaj),
    path('miejsce_id/<slug:PlaceID>', views.miejsce_id),
    path('miejsce_id/<slug:PlaceID>', views.miejsce_id, name='miejsce_id'),
    path('miejsce_id_edytuj/<slug:PlaceID>', views.miejsce_id_edytuj),
    url(r'^o_nas/', views.o_nas),
    url(r'^rejestracja/', views.rejestracja),
    path('trasa_id/<slug:RouteID>', views.trasa_id),
    url(r'^trasa_dodaj/', views.trasa_dodaj),
    path('trasa_id_edytuj/<slug:RouteID>', views.trasa_id_edytuj),
    url(r'^trasy/', views.trasy),
    url(r'^zapomnialem_hasla/', password_reset, {'template_name': 'zapomnialem_hasla.html'}),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', include('app.urls')),
    url(r'^widok_trendow/', views.widok_trendow),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^route-places/(?P<pk>[0-9]+)/$', views.RoutePlaces)
]

urlpatterns += router.urls
