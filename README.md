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
  - `matplotlib`
  - `seaborn`

## Instalación

Desde la raíz del proyecto:

```bash
pip install -r requirements.txt
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
- `src/evaluation.py`: evaluación de métricas y generación de gráficas.
- `data/`: almacenamiento local del CSV.
- `outputs/`: salidas generadas por el pipeline.

## Hallazgos de revisión para salida a producción (universidad)

- ✅ El pipeline principal está completo y funcional en tres etapas: carga/preparación, entrenamiento y evaluación.
- ✅ Se generan artefactos de salida útiles para evidencia académica:
  - `outputs/01_matriz_confusion.png`
  - `outputs/02_arbol_decision.png`
- ⚠️ Dependencia externa crítica: la primera ejecución requiere acceso a Kaggle para descargar datos.
- ⚠️ Para ejecución estable en entorno institucional, se recomienda:
  1. Pre-cargar `data/Admission_Predict.csv` en el servidor.
  2. Ejecutar con entorno virtual y `requirements.txt`.
  3. Definir responsable de validación periódica de métricas del modelo.

## Estado recomendado

**Listo para despliegue académico/institucional controlado**, con la condición de asegurar disponibilidad del dataset y entorno de ejecución reproducible.

## Créditos

- **GitHub Copilot (asistente técnico)**
- **quitian07 (Esteban Quitian)**
- **oscari2606 (Oscar Ivan)**
- **Jhederith**
