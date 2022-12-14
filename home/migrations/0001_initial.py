# Generated by Django 3.2 on 2022-10-04 12:06

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtítulo')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='Blog', variations={'thumb': {'crop': True, 'height': 215, 'width': 351}}, verbose_name='Image')),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
