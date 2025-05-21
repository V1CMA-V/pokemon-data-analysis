import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# --- Configuración inicial de página ---
st.set_page_config(page_title="Clasificador Pokémon Legendarios", page_icon="🧬", layout="wide")

# --- Cargar modelo y columnas ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "..", "models", "xgboost_app_model_clean.pkl"))
model_columns = joblib.load(os.path.join(BASE_DIR, "..", "models", "xgboost_app_model_columns.pkl"))

# --- Datos auxiliares ---
generations = ['generation-i', 'generation-ii', 'generation-iii', 'generation-iv',
               'generation-v', 'generation-vi', 'generation-vii', 'generation-viii', 'generation-ix']
colors = ['red', 'blue', 'yellow', 'green', 'black', 'brown', 'purple', 'gray', 'white', 'pink']
types = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison',
         'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon',
         'dark', 'steel', 'fairy', 'None']

# --- Encabezado y logo ---
st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png", width=120)
st.title("🧬 Clasificador de Pokémon Legendarios")
st.markdown("Introduce las características de un Pokémon para predecir si tiene potencial legendario.")

# --- Modo simple/avanzado ---
modo = st.radio("Selecciona el modo de ingreso:", ["🌟 Modo Simple", "🧠 Modo Avanzado"])

# --- Entradas de usuario ---
with st.form("input_form"):
    if modo == "🌟 Modo Simple":
        base_stat_total = st.slider("Base Stat Total", 200, 800, 500)
        attack = st.slider("Attack", 0, 200, 80)
        catch_rate = st.slider("Catch Rate", 3, 255, 45)
        evolution_stage = st.selectbox("Etapa de evolución", [1, 2, 3])
        primary_type = st.selectbox("Tipo primario", types[:-1])
        generation = st.selectbox("Generación", generations)
        color = st.selectbox("Color", colors)

        # Valores fijos
        defense = 70
        special_attack = 70
        special_defense = 70
        speed = 70
        num_evolution = 2
        has_secondary_type = False
        secondary_type = "None"

    else:  # 🧠 Modo Avanzado
        st.subheader("📊 Estadísticas Base")
        col1, col2 = st.columns(2)
        with col1:
            base_stat_total = st.slider("Base Stat Total", 200, 800, 500)
            attack = st.slider("Attack", 0, 200, 80)
            special_attack = st.slider("Special Attack", 0, 200, 80)
            speed = st.slider("Speed", 0, 200, 80)
        with col2:
            defense = st.slider("Defense", 0, 200, 80)
            special_defense = st.slider("Special Defense", 0, 200, 80)
            catch_rate = st.slider("Catch Rate", 3, 255, 45)

        st.subheader("🧬 Evolución y Rasgos")
        col3, col4 = st.columns(2)
        with col3:
            evolution_stage = st.selectbox("Etapa de evolución", [1, 2, 3])
            has_secondary_type = st.checkbox("¿Tiene Segundo Tipo?", value=True)
        with col4:
            num_evolution = st.selectbox("Cantidad de evoluciones", [1, 2, 3])

        st.subheader("🎨 Tipado y Apariencia")
        col5, col6 = st.columns(2)
        with col5:
            primary_type = st.selectbox("Tipo primario", types[:-1])
            secondary_type = st.selectbox("Tipo secundario", types)
        with col6:
            generation = st.selectbox("Generación", generations)
            color = st.selectbox("Color", colors)

    # Botón para enviar
    submitted = st.form_submit_button("🔍 ¿Es Legendario?")

# --- Procesamiento de inputs ---
if submitted:
    input_dict = {
        "Base Stat Total": base_stat_total,
        "Attack": attack,
        "Defense": defense,
        "Special Attack": special_attack,
        "Special Defense": special_defense,
        "Speed": speed,
        "Catch Rate": catch_rate,
        "Evolution Stage": evolution_stage,
        "Number of Evolution": num_evolution,
        "Secondary Typing Flag": int(has_secondary_type)
    }

    for col in model_columns:
        if col.startswith("Gen_"):
            input_dict[col] = int(col == f"Gen_{generation}")
        elif col.startswith("Color_"):
            input_dict[col] = int(col == f"Color_{color}")
        elif col.startswith("PType_"):
            input_dict[col] = int(col == f"PType_{primary_type}")
        elif col.startswith("SType_"):
            stype_value = secondary_type if has_secondary_type else "None"
            input_dict[col] = int(col == f"SType_{stype_value}")

    input_df = pd.DataFrame([input_dict])[model_columns]

    # --- Predicción ---
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    # --- Resultados visuales ---
    st.markdown("---")
    col_res1, col_res2 = st.columns([1, 2])
    with col_res1:
        if pred == 1:
            st.balloons()
            st.success(f"🦄 ¡Este Pokémon tiene características legendarias!")
        else:
            st.warning(f"🐣 Este Pokémon no parece ser legendario.")

    with col_res2:
        st.metric("Probabilidad de ser legendario", f"{prob:.2%}")
        st.progress(min(int(prob * 100), 100))

    # --- Historial de predicciones ---
    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append({
        "Probabilidad": f"{prob:.2%}",
        "Resultado": "Legendario" if pred else "No legendario"
    })

    st.markdown("### 📈 Historial de predicciones")
    st.dataframe(pd.DataFrame(st.session_state.history).iloc[::-1])

