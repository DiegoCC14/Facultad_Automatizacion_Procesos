from django.urls import path , include
from .views import MD2PDF_Home

urlpatterns = [
    path('md2pdf/', MD2PDF_Home.as_view() , name="md2pdf"),
]
