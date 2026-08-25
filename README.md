# Clasificación de Admisiones de Posgrado

Proyecto en Python para entrenar un modelo de **árbol de decisión** que clasifica si una persona tiene probabilidad de admisión (`yes` / `no`) con base en el dataset de admisiones de posgrado.

## ¿Qué hace este repositorio?

El flujo principal (`main.py`) está pensado para:
1. Descargar/cargar datos de Kaggle.
2. Limpiar columnas y preparar variable objetivo binaria.
3. Entrenar un modelo de clasificación.
4. Evaluar métricas y generar salidas.

## Requisitos

- Python 3.10+ (recomendado)
- Paquetes:
  - `pandas`
  - `scikit-learn`
  - `kagglehub`

## Instalación

Desde la raíz del proyecto:

```bash
pip install pandas scikit-learn kagglehub
```

## Cómo usarlo

### Opción 1: ejecutar el pipeline principal

```bash
python main.py
```

### Opción 2: uso práctico mínimo (carga + entrenamiento)

Si quieres validar rápidamente el flujo base:

```bash
python -c "from src.loader import cargar_y_preparar_datos; from src.model import entrenar_arbol; X_train,X_test,y_train,y_test=cargar_y_preparar_datos(); entrenar_arbol(X_train,y_train); print('Entrenamiento OK')"
```

## Estructura del proyecto

- `main.py`: orquesta el pipeline.
- `src/loader.py`: descarga/carga y prepara el dataset.
- `src/model.py`: entrenamiento del árbol de decisión.
- `src/evaluation.py`: módulo destinado a evaluación.
- `data/`: almacenamiento local del CSV.
- `outputs/`: salidas generadas por el pipeline.

## Nota importante

Actualmente `main.py` importa `evaluar_modelo` desde `src/evaluation.py`. Asegúrate de que ese módulo tenga la función implementada para completar el pipeline de punta a punta.

## Créditos

- Autor original del proyecto: **Jhederith Quitian**
- README en español y guía de uso: **GitHub Copilot**
