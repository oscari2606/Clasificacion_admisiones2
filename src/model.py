from sklearn.tree import DecisionTreeClassifier

def entrenar_arbol(X_train, y_train):
    """
    Inicializa y entrena un modelo de Árbol de Decisión para clasificación.
    """
    print("\n" + "="*50)
    print(" ENTRENAMIENTO DEL ÁRBOL DE CLASIFICACIÓN ")
    print("="*50)
    
    # Definimos el modelo. Usamos random_state para que sea reproducible.
    # Podemos limitar max_depth (ej. 4 o 5) para evitar el sobreajuste (overfitting).
    modelo = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)
    
    # Entrenamos el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)
    
    print("[INFO] Modelo de Árbol de Decisión entrenado exitosamente.")
    return modelo