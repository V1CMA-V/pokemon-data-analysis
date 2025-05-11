# Clasificador de Pokémon Legendarios 🧬

Este proyecto implementa un clasificador de Pokémon legendarios utilizando técnicas de machine learning. La aplicación web permite a los usuarios ingresar características de un Pokémon y predecir si tiene potencial para ser legendario.

## 🌟 Características

- Interfaz web interactiva construida con Streamlit
- Modelo de clasificación XGBoost
- Dos modos de uso:
  - Modo Simple: Para usuarios casuales
  - Modo Avanzado: Para usuarios expertos
- Visualización de predicciones en tiempo real

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/V1CMA-V/pokemon-data-analysis.git
cd pokemon-data-analysis
```

2. Crea un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

Para ejecutar la aplicación web:

```bash
streamlit run src/app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado.

## 📁 Estructura del Proyecto

```
pokemon-data-analysis/
├── data/
│   └── all_pokemon_data.csv    # Dataset de Pokémon
├── models/
│   ├── xgboost_app_model_clean.pkl    # Modelo principal
│   └── xgboost_app_model_columns.pkl  # Columnas del modelo
├── notebooks/
│   └── 01_KDD.ipynb           # Notebook de análisis
├── src/
│   └── app.py                 # Aplicación web
└── README.md
```

## 🛠️ Tecnologías Utilizadas

- Python 3.8+
- Streamlit
- XGBoost
- Pandas
- NumPy
- Joblib

## 📊 Dataset

El proyecto utiliza un conjunto de datos completo de Pokémon que incluye:
- Estadísticas base
- Tipos
- Generación
- Tasas de captura
- Y más características relevantes

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✨ Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 👥 Autores

- [Tu Nombre]

## 🙏 Agradecimientos

- [PokeAPI](https://pokeapi.co/) por los datos de Pokémon
- La comunidad de Pokémon por su continuo apoyo
