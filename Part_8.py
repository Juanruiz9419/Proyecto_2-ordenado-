import pandas as pd
import matplotlib.pyplot as plt

try:
    
    archivo_csv = "heart_failure_clinical_records_dataset.csv"
    dataframe = pd.read_csv(archivo_csv)

    
    anemic_count = dataframe['anaemia'].sum()
    diabetic_count = dataframe['diabetes'].sum()
    smoking_count = dataframe['smoking'].sum()
    death_count = dataframe['DEATH_EVENT'].sum()


    plt.figure(figsize=(12, 6))


    plt.subplot(2, 2, 1)
    labels = ['No ', 'si']
    sizes = [len(dataframe) - anemic_count, anemic_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Anémicos')


    plt.subplot(2, 2, 2)
    labels = ['No ', 'si']
    sizes = [len(dataframe) - diabetic_count, diabetic_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Diabéticos')


    plt.subplot(2, 2, 3)
    labels = ['No ', 'si']
    sizes = [len(dataframe) - smoking_count, smoking_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Fumadores')


    plt.subplot(2, 2, 4)
    labels = ['no', 'si']
    sizes = [len(dataframe) - death_count, death_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Muertos')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")