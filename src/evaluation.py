import os
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import seaborn as sns
 
def evaluar_modelo(modelo, X_test, y_test, feature_names):
    """
    Evalúa el modelo con métricas de clasificación y genera gráficos clave.
    """
    os.makedirs("outputs", exist_ok=True)
    
    print("\n" + "="*50)
    print(" EVALUACIÓN E INTERPRETACIÓN DE RESULTADOS ")
    print("="*50)
    
    # Predicciones sobre el conjunto de prueba
    y_pred = modelo.predict(X_test)
    
    # Métricas principales
    acc = accuracy_score(y_test, y_pred)
    print(f" Exactitud (Accuracy) del Modelo: {acc:.4f}")
    
    print("\n Reporte de Clasificación:")
    print(classification_report(y_test, y_pred))
    
    # 1. Gráfico de la Matriz de Confusión
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax,
                xticklabels=['No (<0.6)', 'Yes (>=0.6)'],
                yticklabels=['No (<0.6)', 'Yes (>=0.6)'])
    ax.set_title('Matriz de Confusión - Árbol de Decisión')
    ax.set_xlabel('Predicción del Modelo')
    ax.set_ylabel('Valor Real')
    
    plt.tight_layout()
    plt.savefig('outputs/01_matriz_confusion.png', dpi=200)
    plt.close()
    
    # 2. Gráfico visual del Árbol de Decisión (para interpretar las reglas)
    fig, ax = plt.subplots(figsize=(16, 10))
    plot_tree(modelo, feature_names=list(feature_names),
              class_names=['No', 'Yes'], filled=True, rounded=True, ax=ax, fontsize=9)
    ax.set_title("Estructura del Árbol de Decisión para Admisiones")
    
    plt.tight_layout()
    plt.savefig('outputs/02_arbol_decision.png', dpi=200)
    plt.close()
    
    print("[INFO] Gráficos de evaluación guardados en la carpeta /outputs.")