from django.urls import path
from .views import ContactPageView
from .views import (
    HomePageView,
    AboutPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/create', ProductCreateView.as_view(), name='form'),


    path('products/', ProductIndexView.as_view(), name='products.index'),
    path('products/create/', ProductCreateView.as_view(), name='products.create'),
    path('products/<str:id>/', ProductShowView.as_view(), name='products.show'),
]

