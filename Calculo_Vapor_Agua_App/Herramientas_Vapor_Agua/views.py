from pathlib import Path
import json , random , string , os , shutil
from .services.csv_service import elimina_columna_de_csv
import pandas as pd

from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , redirect
from django.views import View


CURRENT_DIR = Path(__file__).resolve().parent


class Home( View ):

	def get( self , request ):
		return redirect("analisis_modificasion_csv")


class Analisis_Modificasion_CSV( View ):

	def get( self , request ):
		return render( request , 'elimina_columna.html' )

	def post( self , request ):
		data_post = request.POST.dict()

		columas_a_eliminar = [ cadena.replace('\r',"") for cadena in data_post["text_area_columnas_eliminar"].split('\n') if len( cadena.replace(" ","") ) != 0 ]

		name_temp_dir = ''.join(random.choice( string.ascii_lowercase ) for i in range(4))
		dir_folder_temp_csv = CURRENT_DIR/f'CSV_TEMP/{name_temp_dir}'
		os.mkdir( dir_folder_temp_csv ) #Creamos la carpeta

		for file_csv in request.FILES.getlist('archivos'): #myfile is the name of your html file button
			elimina_columna_de_csv( file_csv , columas_a_eliminar , dir_folder_temp_csv , file_csv.name )
		
		shutil.make_archive( dir_folder_temp_csv , 'zip', dir_folder_temp_csv)
		
		response = HttpResponse(open(f'{dir_folder_temp_csv}.zip', 'rb'), content_type='application/zip')
		response['Content-Disposition'] = f'attachment; filename="{name_temp_dir}.zip"'

		# Borramos las carpetas y los comprimidos generados
		os.remove( f'{dir_folder_temp_csv}.zip' )
		shutil.rmtree( dir_folder_temp_csv )
		# --------------------------------------->>>>>>>>>
		
		return response