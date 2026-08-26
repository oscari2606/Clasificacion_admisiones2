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

## Instalación y puesta en marcha

### 1) Clonar el repositorio

```bash
git clone https://github.com/oscari2606/Clasificacion_admisiones2.git
cd Clasificacion_admisiones2
```

### 2) Crear y activar entorno virtual (venv)

```bash
python -m venv .venv
source .venv/bin/activate
```

> En Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`

### 3) Instalar requerimientos

```bash
pip install -r requirements.txt
```

### 4) Ejecutar el pipeline principal

```bash
python main.py
```

La descarga de datos se realiza automáticamente vía API de Kaggle (a través de `kagglehub`) para mantener el dataset actualizado.

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
- ✅ La estrategia de datos queda alineada con actualización automática desde Kaggle API.
- ⚠️ Para ejecución estable en entorno institucional, se recomienda:
  1. Asegurar conectividad y credenciales de Kaggle en el entorno de ejecución.
  2. Ejecutar con entorno virtual y `requirements.txt`.
  3. Definir responsable de validación periódica de métricas del modelo.

## Estado recomendado

**Listo para despliegue académico/institucional controlado**, con la condición de asegurar disponibilidad del dataset y entorno de ejecución reproducible.

## Créditos

- **GitHub Copilot (asistente técnico)**
- **quitian07 (Esteban Quitian)**
- **oscari2606 (Oscar Ivan)**
- **@jhederith (Jhederith Quitian)**
