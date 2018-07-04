from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^$', views.main, name='main'),
    url(r'^local/$', views.local_list, name="local_list"),
]