from django.urls import path
from . import views


urlpatterns = [

    path('', views.sender.as_view(), name="sender"),

]
