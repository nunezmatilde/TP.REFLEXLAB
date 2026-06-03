import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


from src.validacion_datos import validar_datos
from src.metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error
from src.procesamiento_datos import filtrar_por_participante

st.title("TP ReflexLab")
st.write("Dashboard del proyecto")


archivo = st.file_uploader("Subí el archivo CSV", type=["csv"])

if archivo is not None:
    try:
        df = pd.read_csv(archivo)

        registros = df.to_dict(orient="records")

        registros_validos = []

        for registro in registros:
            if validar_datos(registro):
                registros_validos.append(registro)

        if len(registros_validos) == 0:
            raise ValueError("No hay registros válidos para analizar.")

        st.success("Archivo cargado y validado correctamente")

        st.subheader("Vista previa de los datos")
        st.dataframe(pd.DataFrame(registros_validos).head())

        tiempo_promedio = calcular_tiempo_reaccion_promedio(registros_validos)
        tasa_error = calcular_tasa_error(registros_validos)
        cantidad_registros = len(registros_validos)

        col1, col2, col3 = st.columns(3)

        col1.metric("Registros válidos", cantidad_registros)
        col2.metric("Tiempo promedio", tiempo_promedio)
        col3.metric("Tasa de error", tasa_error)

        st.subheader("Filtrar por participante")

        participantes = pd.DataFrame(registros_validos)["id_participante"].unique()
        participante_elegido = st.selectbox("Elegí un participante", participantes)

        datos_participante = filtrar_por_participante(
            registros_validos,
            participante_elegido
        )

        st.dataframe(pd.DataFrame(datos_participante))

        st.subheader("Gráfico de tiempo de reacción por condición")

        df_validos = pd.DataFrame(registros_validos)

        promedio_condicion = df_validos.groupby("condicion")["tiempo_reaccion"].mean()

        fig, ax = plt.subplots()
        promedio_condicion.plot(kind="bar", ax=ax)

        ax.set_xlabel("Condición")
        ax.set_ylabel("Tiempo de reacción promedio")
        ax.set_title("Tiempo de reacción promedio por condición")

        st.pyplot(fig)

    except ValueError as e:
        st.error(f"Error en el archivo: {e}")

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")