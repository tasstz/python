from django.urls import path
from .views import ProductViewSet, ProductDetailView, ProductAddView


urlpatterns = [
    path('products/', ProductViewSet.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/add', ProductAddView.as_view()),
]