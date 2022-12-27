from django.db import models

# Create your models here.
def object_path(instance, filename):
    return "object/" + str(instance.name) + "/fotka/" + filename


class Object(models.Model):
    name = models.CharField(max_length=50, verbose_name="Jméno:")

    object = models.CharField(max_length=100, verbose_name="Název objektu:")

    photo = models.FileField(upload_to=object_path, blank=True, null=True, verbose_name="Fotka:")

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Objects"

    def __str__(self):
        return self.name