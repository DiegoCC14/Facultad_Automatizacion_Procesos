from django.urls import path
from .views import Envio_Correos_Masivos


urlpatterns = [
    path( 'envio_correos_masivos/' , Envio_Correos_Masivos.as_view() , name='envio_correos_masivos' ),
]
