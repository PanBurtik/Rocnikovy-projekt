from django.db import models

# Create your models here.
def object_path(instance, filename):
    return str(instance.object) + "/fotka/" + filename

def zip_path(instance, filename):
    return str(instance.name) + "/zip/" + filename

def texture_path(instance, filename):
    return str(instance.object_id.object) + "/textures/" + filename

def model_path(instance, filename):
    return str(instance.object) + "/" + filename



class Object(models.Model):
    name = models.CharField(max_length=50, verbose_name="Jméno:")

    object = models.CharField(unique=True,max_length=100, verbose_name="Název objektu:")
    
    description = models.TextField(blank=True, null = True, verbose_name="Popis objektu:")

    photo = models.FileField(upload_to=object_path, blank=True, null=True, verbose_name="Fotka:")

    scene_bin = models.FileField(upload_to=model_path, null=True, verbose_name="BIN soubor:")

    scene_gltf = models.FileField(upload_to=model_path, null=True, verbose_name="GLTF soubor:")
    

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Objects"

    def __str__(self):
        return self.name


class Textures(models.Model):

    textures = models.ImageField(upload_to=texture_path, null=True)

    object_id = models.ForeignKey(Object, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.textures.url