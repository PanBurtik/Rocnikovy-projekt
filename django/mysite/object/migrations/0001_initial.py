# Generated by Django 4.1.4 on 2022-12-21 21:31

from django.db import migrations, models
import object.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Jméno:')),
                ('object', models.CharField(max_length=100, verbose_name='Název objektu:')),
                ('photo', models.FileField(blank=True, null=True, upload_to=object.models.object_path, verbose_name='Fotka:')),
            ],
            options={
                'verbose_name_plural': 'Objects',
                'ordering': ['name'],
            },
        ),
    ]