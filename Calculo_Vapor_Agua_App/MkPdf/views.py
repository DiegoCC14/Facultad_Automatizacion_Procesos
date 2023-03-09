from pathlib import Path
import markdown , shutil , os , random , string
from .services.conversor import read_file_markdown , moficar_syle_html , convertir_markdown_a_pdf

from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , redirect
from django.views import View
from django.core.files.storage import default_storage


CURRENT_DIR = Path(__file__).resolve().parent


def guardar_archivo( archivo , ruta_carpeta ):
    nombre_archivo = archivo.name
    ruta_guardado = default_storage.save(f"{ruta_carpeta}/{nombre_archivo}", archivo)
    return ruta_guardado

def delete_file( path_file ):
	os.remove( path_file )

class MD2PDF_Home( View ):
	def get( self , request ):
		return render( request , "md2pdf.html")

	def post( self , request ):
		request_data = request.POST.dict()
		name_pdf = ''.join(random.choice( string.ascii_lowercase ) for i in range(4)) + ".pdf"
		
		if len( request.FILES.getlist('md_file') ) > 0:
			file_md = request.FILES.getlist('md_file')[0] #Tomamos el primer elemento
			name_pdf = file_md.name.replace(".md",".pdf")
			ruta_file_md = guardar_archivo( file_md , CURRENT_DIR/"temp_files" )
			string_markdown = read_file_markdown( ruta_file_md ) #Leemos el archivo .md
			delete_file( ruta_file_md ) #Borramos el archivo para no ocupar espacio
		else:
			string_markdown = request_data["md_text"]

		dicc_styles = {'font-family':request_data["font_family"] , "font-size":request_data["font_size"] , "page_size":request_data["page_size"] }
		convertir_markdown_a_pdf( string_markdown , name_pdf , CURRENT_DIR/"temp_files" , dicc_styles )
		
		with open( CURRENT_DIR/f"temp_files/{name_pdf}" , "rb") as file:
			response = HttpResponse( file , content_type='application/pdf')
			response['Content-Disposition'] = f'attachment; filename="{name_pdf}"'
		
		delete_file( CURRENT_DIR/f"temp_files/{name_pdf}" ) #Borramos el archivo para no ocupar espacio

		return response