from django.urls import path
from .views import Analisis_Modificasion_CSV , Home


urlpatterns = [
    path( '' , Home.as_view() , name='Home' ),
    path( 'analisis_modificasion_csv/' , Analisis_Modificasion_CSV.as_view() , name='analisis_modificasion_csv' ),
]
