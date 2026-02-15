import streamlit as st
import requests
import pandas as pd

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Crop Yield App",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Crop Yield - Prédiction & Recommandation")
st.write("Cette application interroge une API FastAPI pour prédire le rendement ou recommander la meilleure culture.")

# ⚠️ Mets ici l'URL de ton API FastAPI
API_URL = "http://127.0.0.1:8000"

# -----------------------------
# MENU MODE
# -----------------------------
mode = st.radio("Choisis un mode :", ["Prédiction", "Recommandation"], horizontal=True)

st.divider()

# -----------------------------
# INPUTS COMMUNS
# -----------------------------
st.subheader("📌 Contexte")

area = st.text_input("Area (pays)", value="Albania")
year = st.number_input("Year", min_value=1990, max_value=2030, value=2010, step=1)

rain = st.slider("🌧️ Rainfall (mm/an)", min_value=0.0, max_value=3500.0, value=1000.0, step=10.0)
temp = st.slider("🌡️ Température moyenne (°C)", min_value=-5.0, max_value=40.0, value=20.0, step=0.5)

pesticides = st.number_input("🧪 Pesticides (tonnes)", min_value=0.0, value=500.0, step=10.0)

fertilizer = st.slider("🌱 Fertilizer_Used", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
irrigation = st.slider("💧 Irrigation_Used", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

days = st.slider("📅 Days_to_Harvest", min_value=80.0, max_value=150.0, value=105.0, step=1.0)


# -----------------------------
# MODE PREDICTION
# -----------------------------
if mode == "Prédiction":
    st.subheader("🎯 Prédire le rendement")

    item = st.text_input("Item (culture)", value="Maize")

    payload = {
        "Item": item,
        "Area": area,
        "Year": int(year),
        "average_rain_fall_mm_per_year": float(rain),
        "avg_temp": float(temp),
        "Pesticide_use_total_tonnes": float(pesticides),
        "Fertilizer_Used": float(fertilizer),
        "Irrigation_Used": float(irrigation),
        "Days_to_Harvest": float(days)
    }

    if st.button("🚀 Lancer la prédiction"):
        try:
            response = requests.post(f"{API_URL}/predict", json=payload)

            if response.status_code == 200:
                result = response.json()
                pred = result.get("predicted_yield_hg_per_ha", None)

                st.success("✅ Prédiction réussie !")

                if pred is not None:
                    st.metric("Rendement prédit (hg/ha)", pred)
                else:
                    st.warning("Le champ predicted_yield_hg_per_ha est introuvable dans la réponse API.")

            else:
                st.error(f"❌ Erreur API : {response.status_code}")
                st.code(response.text)

        except Exception as e:
            st.error("❌ Impossible de contacter l'API FastAPI.")
            st.write(e)


# -----------------------------
# MODE RECOMMANDATION
# -----------------------------
else:
    st.subheader("⭐ Recommander la meilleure culture")

    payload = {
        "Area": area,
        "Year": int(year),
        "average_rain_fall_mm_per_year": float(rain),
        "avg_temp": float(temp),
        "Pesticide_use_total_tonnes": float(pesticides),
        "Fertilizer_Used": float(fertilizer),
        "Irrigation_Used": float(irrigation),
        "Days_to_Harvest": float(days)
    }

    if st.button("🚀 Lancer la recommandation"):
        try:
            response = requests.post(f"{API_URL}/recommend", json=payload)

            if response.status_code == 200:
                results = response.json()

                st.success("✅ Recommandation réussie !")

                df = pd.DataFrame(results)

                # Tableau
                st.subheader("📋 Tableau des rendements")
                st.dataframe(df, use_container_width=True)

                # Graphique barres
                st.subheader("📊 Comparaison des rendements")
                df_plot = df.set_index("crop")
                st.bar_chart(df_plot["predicted_yield_hg_per_ha"])

                # Meilleure culture
                best = df.iloc[0]
                st.info(f"🏆 Culture recommandée : **{best['crop']}** (rendement : {best['predicted_yield_hg_per_ha']} hg/ha)")

            else:
                st.error(f"❌ Erreur API : {response.status_code}")
                st.code(response.text)

        except Exception as e:
            st.error("❌ Impossible de contacter l'API FastAPI.")
            st.write(e)
