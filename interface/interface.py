import os
import sys
import streamlit as st
import numpy as np

# Añadir la raíz del repositorio (donde está `src/`) a sys.path para permitir imports
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.poissonSL import calcular_probabilidad_por_tipo


st.set_page_config(page_title="Distribución de Poisson", layout="centered")

# Ocultar menú y footer y la barra lateral para apariencia minimalista
HIDE_STREAMLIT_STYLE = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stSidebar {display: none;}
</style>
"""
st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)




def main():
    # Centrar el contenido con columnas: la UI va en la columna central
    izq, centro, der = st.columns([1, 2, 1])
    with centro:
        st.title("Calculadora de Distribución de Poisson")

        with st.form(key="poisson_form"):
            mu_texto = st.text_input("Media o valor esperado (μ)", value="4.0")
            x = st.number_input("x (ocurrencias)", min_value=0, value=3, step=1)

            tipo = st.radio(
                "Tipo de probabilidad",
                options=[
                    (1, "X = x"),
                    (2, "X < x"),
                    (3, "X ≤ x"),
                    (4, "X > x"),
                    (5, "X ≥ x"),
                ],
                format_func=lambda t: t[1],
            )

            calcular = st.form_submit_button("Calcular")

        if calcular:
            # Validar μ
            try:
                mu = float(mu_texto)
                if mu <= 0:
                    raise ValueError()
            except Exception:
                st.error("Media o valor esperado (μ) debe ser un número > 0")
                return

            opcion = int(tipo[0])
            probabilidad = calcular_probabilidad_por_tipo(mu, int(x), opcion)
            st.markdown(f"### Resultado: **{probabilidad*100:.2f}%**")

           

    # left/right quedan vacíos solo para centrar


if __name__ == "__main__":
    main()
