from rest_framework import serializers
from .models import Category, SubCategory, Product, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    #category = CategorySerializer()
    class Meta:
        model = SubCategory
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    category = serializers.CharField(source='sub_category.category.name')
    sub_category = serializers.CharField(source='sub_category.name')
    class Meta:
        model = Product
        fields = '__all__'