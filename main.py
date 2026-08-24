from src.loader import cargar_y_preparar_datos
from src.model import entrenar_arbol
from src.evaluation import evaluar_modelo

def main():
    print("=" * 70)
    print(" PIPELINE DE CLASIFICACIÓN - ADMISIONES DE POSGRADO ")
    print("=" * 70)
    
    # 1. Cargar, limpiar y preparar particiones
    X_train, X_test, y_train, y_test = cargar_y_preparar_datos()
    
    # 2. Entrenar el modelo de Árbol de Clasificación
    modelo = entrenar_arbol(X_train, y_train)
    
    # 3. Evaluar métricas y generar outputs visuales
    evaluar_modelo(modelo, X_test, y_test, X_train.columns)
    
    print("\n" + "=" * 70)
    print("[EXITO] Proceso completado sin errores.")
    print("=" * 70)

if __name__ == "__main__":
    main()