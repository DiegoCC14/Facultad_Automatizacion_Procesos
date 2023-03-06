from pathlib import Path
import zipfile


BASE_DIR = Path(__file__).resolve().parent


def unzip( file_path , extract_path ):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

if __name__ == "__main__":
    unzip( 'Data_Prueba.zip' , BASE_DIR/"Data_Prueba" )