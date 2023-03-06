from pathlib import Path
import json , random , string , os , shutil
from .services.csv_service import elimina_columna_de_csv
from .services.descomprecion_file_services import unzip
from .services.search_files import find_extencion_files_recursively
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

		if data_post[ 'tipo_archivo' ] == 'csv_files':

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

		elif data_post[ 'tipo_archivo' ] == 'zip_file':
				
			file_rar = request.FILES.getlist('archivos')[0] #ZIP subido
			dir_file_unzip = CURRENT_DIR/f"ZIP_TEMP/{file_rar.name.replace('.','_') + name_temp_dir}"
			unzip( file_rar , dir_file_unzip ) #Descomprimimos el archivo .ZIP
			
			for file_csv in find_extencion_files_recursively( dir_file_unzip , ".csv" ): #Buscamos los csv dentro de una carpeta
				elimina_columna_de_csv( file_csv , columas_a_eliminar , Path( os.path.dirname( file_csv ) ) , file_csv.name )

			shutil.make_archive( dir_file_unzip , 'zip', dir_file_unzip)

			response = HttpResponse(open(f'{dir_file_unzip}.zip', 'rb'), content_type='application/zip')
			response['Content-Disposition'] = f'attachment; filename="{name_temp_dir}.zip"'

			# Borramos las carpetas y los comprimidos generados
			os.remove( f'{dir_file_unzip}.zip' )
			shutil.rmtree( dir_file_unzip )
			# --------------------------------------->>>>>>>>>
			return response