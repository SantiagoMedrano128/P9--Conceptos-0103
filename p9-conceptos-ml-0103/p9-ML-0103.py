#Santiago Medrano Segundo 0103
import pandas as pd
print(pd.__version__) # Output: 1.5.2

import pandas as pd

# 11.
datos11 = {
    'distancia_km': [1.1, 3.8, 6.4, 2.5, 4.6],
    'trafico_nivel': [1, 2, 3, 1, 3],
    'edad_repartidor': [21, 34, 42, 29, 37],
    'tiempo_entrega_min': [9, 28, 60, 18, 44]
}

df = pd.DataFrame(datos11)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Santiago medrano 0103")