from django.views.generic import ListView
from multiprocessing import context
from django.shortcuts import render, redirect
from object.models import Object
from django.contrib.auth.forms import UserCreationForm

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

def model(request):
    return render(request, 'model.html')

class ObjectListView(ListView):
    model = Object

    context_object_name = 'objects'
    template_name = 'list.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):

    return render(request, 'login.html')