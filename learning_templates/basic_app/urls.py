from django.urls import path
from basic_app import views

app_name = 'basic_apps'

urlpatterns = [
    path('other', views.other, name='other'),
    path('relevent', views.relevent, name='relevent'),
]
