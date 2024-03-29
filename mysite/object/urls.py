from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('model/<str:model_name>', views.model, name='model'),
    path('add-object/', views.addObject, name='add-obj'),
    path('reset-password/',views.reset, name='reset'),

]