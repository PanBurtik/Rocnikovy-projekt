from multiprocessing import context
from django.shortcuts import render, redirect
from object.models import Object, Textures
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request): 

    num_objects = Object.objects.all().count

    objects = Object.objects.order_by('name')

    context ={
        'num_objects': num_objects,
        'objects': objects,
    }
    
    return render(request, 'index.html', context = context)

    
def home(request):
    return render(request, 'index.html')


def model(request, model_name):
    return render(request, 'model.html', {"object": model_name})


def addObject(request):
    if request.method == "POST":
            prod = Object()
            prod.name = request.POST.get('name')
            prod.object = request.POST.get('object')
            prod.description = request.POST.get('description')

            if len(request.FILES) != 0:
                prod.photo = request.FILES['photo']

            if len(request.FILES) != 0:
                prod.scene_bin = request.FILES['scene_bin']
            if len(request.FILES) != 0:
                prod.scene_gltf = request.FILES['scene_gltf']

            prod.save()
            def save_texture(img):
                Textures.objects.create(textures = img, object_id = prod)
                print(img)
            f = [save_texture(x) for x in request.FILES.getlist('textures')]

            
            messages.success(request, 'Objekt byl přidán do databáze')
            return redirect('/')

    

    return render(request, 'addObj.html')


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

def reset(request):
    return render(request, 'reset.html')