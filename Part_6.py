import argparse
import pandas as pd
import requests
import io


parser = argparse.ArgumentParser(description="Descargar datos CSV desde una URL y categorizarlos.")


parser.add_argument("url", help="")


args = parser.parse_args()

try:
    url_datos = args.url
    response = requests.get(url_datos)
    
    # Verificar si la solicitud fue exitosa
    response.raise_for_status()
    
    # Cambiar el tipo de contenido a "text/csv" para cargar los datos correctamente
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    
    
    dataframe = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    
    # Categorizar
    bins = [0, 30, 60, float('inf')]
    labels = ['Joven', 'Adulto', 'Mayor']
    dataframe['Grupo de Edad'] = pd.cut(dataframe['age'], bins=bins, labels=labels)
    
    print("Datos descargados y convertidos en un DataFrame:")
    print(dataframe)
    
    # Guardar el DataFrame 
    dataframe.to_csv("datos_categorizados.csv", index=False)
    
    print("Los datos han sido guardados en 'datos_categorizados.csv'")
    
except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")