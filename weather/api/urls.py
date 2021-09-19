from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'locations/$', views.LocationList, name='locations'),
    url(r'locations/<int:pk>/$', views.LocationDetail, name='detail'),
]