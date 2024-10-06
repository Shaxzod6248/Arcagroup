from rest_framework import serializers
from product.models import Category, Products, Banner

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        depth = 1
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'