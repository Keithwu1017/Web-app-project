# Generated by Django 5.0.1 on 2024-05-12 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PictureBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('n_pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField()),
                ('image', models.ImageField(upload_to='book_pictures/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='library.picturebook')),
            ],
            options={
                'ordering': ['page_number'],
            },
        ),
    ]