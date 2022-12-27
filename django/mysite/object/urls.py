from django.urls import path
from . import views

urlpatterns = [
    path('', views.ObjectListView.as_view(), name="objects"),

]