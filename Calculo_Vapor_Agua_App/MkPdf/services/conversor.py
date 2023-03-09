# -*- coding: utf-8 -*-
import markdown
from xhtml2pdf import pisa

def read_file_markdown( path_file ):
    #lee el markdown y retorna su string
    try:
        #Codificado en Latin-8
        with open( path_file , 'r', encoding="ISO-8859-1") as f:
            markdown_string = f.read()
        return markdown_string
    except:
        try:
            #Codificado en UTF-8
            with open( path_file , 'r', encoding='utf-8') as f:
                markdown_string = f.read()
            return markdown_string
        except :
            return TypeError

def moficar_syle_html( html_string , dicc_style ):
    '''
    {
        "page_size":"A4",
        "font-family:"Arial",
        "font-size": "12px",
    }
    
    body { //
        font-family: Arial, sans-serif;
        font-size: 16px;
        line-height: 1.5;
    }

    p { //
      margin-bottom: 1em;
    }

    ul, ol { //
      margin: 0;
      padding: 0;
      margin-bottom: 1em;
    }
    
    li { //
      margin-bottom: 0.5em;
    }

    a {
      color: #007bff;
      text-decoration: underline;
    }
    
    a:hover {
      color: #0056b3;
    }
    '''
    style_hmtl = "<head><style>"
    style_hmtl += "body { " + f"font-family: {dicc_style['font-family']}, sans-serif; font-size: {dicc_style['font-size']}; line-height: 1.5;" + " } "
    style_hmtl += "h1 { font-size: 24px; font-weight: bold; } p { margin-bottom: 1em; } ul, ol { margin: 0; padding: 0; margin-bottom: 1em; } "
    style_hmtl += "li { margin-bottom: 0.5em; } a { color: #007bff; text-decoration: underline;} a:hover { color: #0056b3; } "
    style_hmtl += "@page { size:" + f"{ dicc_style['page_size'] }; margin: 2cm;" + " }"
    style_hmtl += "</style></head>"
    return ( style_hmtl + html_string )

def convertir_markdown_a_pdf( markdown_string , name_salida , ruta_salida , dicc_styles ):
    html_string = markdown.markdown( markdown_string )
    html_string = moficar_syle_html( html_string , dicc_styles )

    # Crear un archivo PDF a partir de HTML
    with open(ruta_salida/name_salida, "wb") as f:
        pisa.CreatePDF( html_string , dest=f)


if __name__ == "__main__":

    markdown_string = read_file_markdown( "readme.md" )

    # Convertir Markdown a HTML
    html_string = markdown.markdown( markdown_string )

    # Agregamos estilo CSS al archivo html
    html_string = moficar_syle_html( html_string , {"Diego":"Cazon" , "Buenas":"Noches" } )

    # Crear un archivo PDF a partir de HTML
    output_filename = "output.pdf"
    with open(output_filename, "wb") as f:
        #pisa.CreatePDF(style_hmtl+html_string, dest=f)
        pisa.CreatePDF(html_string, dest=f)