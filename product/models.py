from django.db import models
from rest_framework import permissions
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name_uz = models.CharField(max_length=300)
    name_ru = models.CharField(max_length=400)

    def __str__(self):
        return self.name_uz


class Products(models.Model):
    models.ImageField(upload_to="Arcaimg")
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=300)
    descriotion_uz = models.TextField()
    description_ru = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_uz


class Banner(models.Model):
    image = models.ImageField(upload_to="Bannerimg")

    def __str__(self):
        return 'Picbanner'