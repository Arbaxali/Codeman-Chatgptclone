from django.urls import path
from . import views

app_name = "codemanapp"

urlpatterns = [
    path('home/',views.home, name='home'),  
    path('suggest/',views.suggest, name='suggest'),  
]
