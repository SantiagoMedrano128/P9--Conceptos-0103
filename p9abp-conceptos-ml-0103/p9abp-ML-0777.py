import pandas as pd
print(pd.__version__) # Output: 1.5.2

import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Crear un dataset de ejemplo con la estructura especificada
data = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 30, 60, 25, 50],
    'nivel_glucosa': [140, 85, 200, 90, 160],
    'presion_arterial': [80, 70, 95, 65, 85],
    'indice_masa_corporal': [28.5, 22.0, 33.1, 21.4, 30.2],
    'diagnostico_diabetes': [1, 0, 1, 0, 1]  # 1: Diabetes, 0: No Diabetes
}

df = pd.DataFrame(data)

# 2. Eliminar la columna 'id_paciente' (no aporta valor predictivo)
df_limpio = df.drop(columns=['id_paciente'])

# 3. Separar en Features (X) y Target (y)
X = df_limpio.drop(columns=['diagnostico_diabetes'])  # Variables de entrada
y = df_limpio['diagnostico_diabetes']                 # Variable a predecir

# 4. Dividir en conjuntos de Entrenamiento (80%) y Prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Mostrar resultados en consola
print("--- CARACTERÍSTICAS (X) ---")
print(X)
print("\n--- VARIABLE OBJETIVO (y) ---")
print(y)