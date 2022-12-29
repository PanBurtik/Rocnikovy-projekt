from django.views.generic import ListView
from multiprocessing import context
from django.shortcuts import render
from object.models import Object

# Create your views here.
def index(request): 
    
    if request.method == 'POST':
        name = request.POST['name']
        object = request.POST['object']
        description = request.POST['description']
        photo = request.POST['photo']


        new_object = Object(name = name, object = object, description = description, photo = photo)
        new_object.save()



    num_objects = Object.objects.all().count

    objects = Object.objects.order_by('-name')

    context ={
        'num_objects': num_objects,
        'objects': objects,
    }

    return render(request, 'index.html', context = context)

    
def home(request):
    return render(request, 'index.html')

class ObjectListView(ListView):
    model = Object

    context_object_name = 'objects'
    template_name = 'list.html'
