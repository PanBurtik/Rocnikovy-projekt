# Generated by Django 4.1.4 on 2023-01-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0015_textures_object_textures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='textures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.textures'),
        ),
    ]
