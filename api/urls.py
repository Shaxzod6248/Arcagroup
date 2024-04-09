from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import CategoryAPIView, ProductsAPIView, BannerAPIView, ProductsDetail, CategoriesDetail


urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('products/', ProductsAPIView.as_view()),
    path('banners/', BannerAPIView.as_view()),
    path('products/<int:pk>/', ProductsDetail.as_view()),
    path('categories/<int:pk>/', CategoriesDetail.as_view()),
]