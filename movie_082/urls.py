from django.urls import path, include
from .views import home, movieadd, movieupdate

urlpatterns = [

    path('',home, name='home'),
    path('add/',movieadd, name='add'),
    path('update/<str:pk>',movieupdate, name='update'),

]