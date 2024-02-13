from django.urls import path
from .views import detect_unauthorized_sales

urlpatterns = [
    path('detect_unauthorized_sales/', detect_unauthorized_sales, name='detect_unauthorized_sales'),
]
