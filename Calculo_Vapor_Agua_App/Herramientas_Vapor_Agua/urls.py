from django.urls import path
from .views import Analisis_Modificasion_CSV , Home , Obtener_Manual_Uso_CSV_Modificador


urlpatterns = [
    path( '' , Home.as_view() , name='Home' ),
    path( 'analisis_modificasion_csv/' , Analisis_Modificasion_CSV.as_view() , name='analisis_modificasion_csv' ),
    path( 'manual_modificasion_csv/' , Obtener_Manual_Uso_CSV_Modificador.as_view() , name='manual_modificasion_csv' ),
]
