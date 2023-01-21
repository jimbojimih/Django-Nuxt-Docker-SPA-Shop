from rest_framework import viewsets
from .serializers import (
	CategorySerializer, 
	SubCategorySerializer, 
	ProductSerializer, 
)
from .models import Category, SubCategory, Product


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):	
	serializer_class = SubCategorySerializer

	def get_queryset(self):
		queryset = SubCategory.objects.all().order_by('name')
		category = self.request.query_params.get('category')
		if category:
			queryset = queryset.filter(category__name=category)
		return queryset


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):	
	serializer_class = ProductSerializer

	def get_queryset(self):
		queryset = Product.objects.all().order_by('-available')
		category = self.request.query_params.get('category')
		if category:
			queryset = queryset.filter(sub_category__category__name=category)
		return queryset
