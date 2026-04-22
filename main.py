from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante, obtener_ids_participantes
from src.metricas import (
    calcular_tiempo_reaccion_promedio,
    calcular_tasa_error,
  
)

RUTA_DATOS = "ReflexLab_mock_data.csv"


def mostrar_resultados(id_participante: int, datos_participante: list):
    """
    Imprime en pantalla las métricas calculadas para un participante.

    Parámetros:
    - id_participante: identificador del participante
    - datos_participante: lista de registros de ese participante
    """
    tr_promedio = calcular_tiempo_reaccion_promedio(datos_participante)
    tasa_error  = calcular_tasa_error(datos_participante)
  

    print(f"  Trials analizados:            {len(datos_participante)}")
    print(f"  Tiempo de reacción promedio:  {tr_promedio:.3f} s")
    print(f"  Tasa de error:                {tasa_error * 100:.1f}%")
 


def main():
    print("=== ReflexLab — Análisis de datos ===\n")

    # 1. Cargar datos
    print(f"Cargando datos desde '{RUTA_DATOS}'...")
    datos = cargar_datos(RUTA_DATOS)
    print(f"  {len(datos)} trials cargados.\n")

    # 2. Validar datos
    print("Validando registros...")
    datos_validos = []
    datos_invalidos = 0
    for registro in datos:
        if validar_registro(registro):
            datos_validos.append(registro)
        else:
            datos_invalidos += 1

    print(f"  Válidos:   {len(datos_validos)}")
    print(f"  Inválidos: {datos_invalidos}\n")

    # 3. Procesar y analizar por participante
    ids = obtener_ids_participantes(datos_validos)
    print(f"Participantes encontrados: {ids}\n")

    for id_p in ids:
        print(f"--- Participante {id_p} ---")
        datos_participante = filtrar_por_participante(datos_validos, id_p)

        # 4. Mostrar resultados
        mostrar_resultados(id_p, datos_participante)
        print()

    print("=== Análisis finalizado ===")


main()

