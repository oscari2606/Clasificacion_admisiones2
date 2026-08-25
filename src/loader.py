import os
import shutil
import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split

def cargar_y_preparar_datos():
    """
    Descarga el dataset desde Kaggle, verifica nulos, transforma la variable 
    objetivo a categórica binaria y divide el conjunto en train y test.
    """
    os.makedirs("data", exist_ok=True)
    ruta_local_csv = os.path.join("data", "Admission_Predict.csv")
    
    # Descarga automatizada si no existe localmente
    if not os.path.exists(ruta_local_csv):
        print("[INFO] Descargando dataset desde Kaggle...")
        path_kaggle = kagglehub.dataset_download("mohansacharya/graduate-admissions")
        for archivo in os.listdir(path_kaggle):
            if archivo.endswith(".csv"):
                shutil.copy(os.path.join(path_kaggle, archivo), ruta_local_csv)
                break
                
    df = pd.read_csv(ruta_local_csv)
    
    # Limpieza de nombres de columnas (quitar espacios en blanco que trae este dataset de Kaggle)
    df.columns = df.columns.str.strip()
    
    print(f"[INFO] Dimensiones del dataset: {df.shape[0]} filas x {df.shape[1]} columnas")
    
    # Verificación de valores faltantes (Justificación técnica)
    nulos = df.isnull().sum().sum()
    if nulos == 0:
        print("[INFO] No se encontraron valores faltantes en el dataset.")
    else:
        print(f"[WARNING] Se encontraron {nulos} valores nulos. Se requiere imputación.")
        # df.fillna(df.median(), inplace=True) # Opcional si hubiera nulos

    # ELIMINAR COLUMNAS INNECESARIAS: 'Serial No.' es solo un índice, no aporta al modelo.
    if 'Serial No.' in df.columns:
        df = df.drop(columns=['Serial No.'])

    # TRANSFORMACIÓN DE LA VARIABLE OBJETIVO (Requisito del taller)
    # Si 'Chance of Admit' es >= 0.6 -> 'yes', sino 'no'
    target_col = 'Chance of Admit'
    df['admitido_binario'] = df[target_col].apply(lambda x: 'yes' if x >= 0.6 else 'no')
    
    # Separar características (X) y objetivo (y)
    # Ojo: eliminamos la columna original continua y la nueva binaria de X
    X = df.drop(columns=[target_col, 'admitido_binario'])
    y = df['admitido_binario']
    
    # División en conjunto de entrenamiento (80%) y prueba (20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"[INFO] Conjunto de entrenamiento: {len(X_train)} obs. | Validación: {len(X_test)} obs.")
    
    return X_train, X_test, y_train, y_test
