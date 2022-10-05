# Generated by Django 3.2 on 2022-10-04 16:29

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Coleções')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='Blog', variations={'thumb': {'crop': True, 'height': 215, 'width': 351}}, verbose_name='Image')),
            ],
        ),
    ]