# Generated by Django 3.2.9 on 2022-01-26 05:42

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('screenshot', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('site_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('project', models.ForeignKey(default='HTML', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='my_portfolio.projects')),
            ],
        ),
    ]
