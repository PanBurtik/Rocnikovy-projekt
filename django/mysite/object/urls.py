from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('model/', views.model, name='model'),
    path('add-object/', views.addObject, name='add-obj'),

]