from pathlib import Path

from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , redirect
from django.views import View



class Envio_Correos_Masivos( View ):
	
	def get( self , request ):
		return render( request , "envio_correo_masivos.html" )
