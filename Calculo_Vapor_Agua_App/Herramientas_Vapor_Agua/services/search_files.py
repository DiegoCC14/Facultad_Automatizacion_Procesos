from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent


def find_files( path , extencion_file ):
    # extencion_file = .extencion   -> ejemplo: .csv , .zip , .txt
    return [ file for file in os.listdir(path) if file.endswith( extencion_file ) ]


def find_extencion_files_recursively( path , extencion ):
    # extencion_file = .extencion   -> ejemplo: .csv , .zip , .txt

    extencion_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith( extencion ):
                extencion_files.append( BASE_DIR/os.path.join(root, file) ) #Retornoa la ruta completa de el archivo
    return extencion_files

if __name__ == "__main__":
    pass
    #print( [ name_dir.replace(f"\\","/") for name_dir in find_csv_files_recursively( "Data_Prueba" ) ] )