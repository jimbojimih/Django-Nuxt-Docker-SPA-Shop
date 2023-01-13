from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'sub_category', views.SubCategoryViewSet, basename="sub_category")
router.register(r'products', views.ProductCategoryViewSet, basename="products")

urlpatterns = [
        path('', include(router.urls)),
]
