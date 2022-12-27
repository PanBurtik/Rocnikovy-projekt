from django.views.generic import ListView
from django.shortcuts import render
from multiprocessing import context
from object.models import Object

# Create your views here.
class ObjectListView(ListView):
    model = Object

    context_object_name = 'objects'
    template_name = 'list.html'