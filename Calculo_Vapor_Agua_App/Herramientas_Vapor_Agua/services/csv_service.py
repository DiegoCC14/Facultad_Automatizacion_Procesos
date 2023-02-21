from pathlib import Path
import pandas as pd , shutil , os


BASE_DIR = Path(__file__).resolve().parent


def get_columnas_csv( dir_file_csv ):
	df = pd.read_csv( dir_file_csv )
	return list(df.columns)


def elimina_columna_de_csv( file_csv , list_columnas_delete , dir_carpeta_guardado , name_salida ):
	df = pd.read_csv( file_csv )
	df = df.drop( columns=list_columnas_delete )
	df.to_csv( dir_carpeta_guardado/name_salida, index=False )


if __name__ == "__main__":
	dir_file_csv_prueba = 'D:\\Proyectos_Particulares\\Proyecto_Automatizacion_Calculo_Vapor_Agua\\Documentacion\\Data_Prueba\\2238\\AACR2238.csv'
	#list_name_columna = get_columnas_csv( dir_file_csv_prueba )
	#print( f'{list_name_columna}\nTipo:{type( list_name_columna[0] )}' )

	#elimina_columna_de_csv( dir_file_csv_prueba , [ 'IWV' , 'ZTD' ] , BASE_DIR , "AACR2238.csv" )
	os.remove( "D:\\Proyectos_Particulares\\Proyecto_Automatizacion_Calculo_Vapor_Agua\\Calculo_Vapor_Agua_App\\Herramientas_Vapor_Agua\\CSV_TEMP\\illvbpkb.zip" )
	shutil.rmtree("D:\\Proyectos_Particulares\\Proyecto_Automatizacion_Calculo_Vapor_Agua\\Calculo_Vapor_Agua_App\\Herramientas_Vapor_Agua\\CSV_TEMP\\illvbpkb")
