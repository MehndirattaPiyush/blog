from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/',views.login),
    url(r'^$',views.home),
    url(r'^$',views.index),
]
