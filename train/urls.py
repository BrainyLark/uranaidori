from django.urls import path
from . import views

app_name = "train"
urlpatterns = [
     path('', views.index, name="index")
]
