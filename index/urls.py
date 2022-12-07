from unicodedata import name
from django.urls import path 
from index import views

urlpatterns = [
    path('' ,views.Home , name="Home" ),
    path('home' , views.Home , name="Home"),
    
]
