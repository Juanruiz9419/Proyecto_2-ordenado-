import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px


url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
df = pd.read_csv(url)


df = df.drop_duplicates()
df = df.sort_values(by='columna_de_orden', ascending=True)  # Reemplaza 'columna_de_orden' por la columna adecuada


X = df.drop(columns=['DEATH_EVENT', 'categoria_edad']).values


y = df['DEATH_EVENT'].values

# Ejecutar el t-SNE 
X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

#  DataFrame 
df_embedded = pd.DataFrame(X_embedded, columns=['X_embedded_1', 'X_embedded_2', 'X_embedded_3'])
df_embedded['DEATH_EVENT'] = y

# Crear el gráfic
fig = px.scatter_3d(
    df_embedded,
    x='X_embedded_1',
    y='X_embedded_2',
    z='X_embedded_3',
    color='DEATH_EVENT',
    color_continuous_scale='Viridis',  # Puedes ajustar la paleta de colores
    labels={'DEATH_EVENT': 'Death Event'}
)

fig.show()