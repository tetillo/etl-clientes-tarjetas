from src.utils.logger import obtener_logger
from src.utils.file_utils import listar_csv

from src.etl.extract import leer_csv
from src.etl.transform import limpiar
from src.etl.validate import separar_validos_invalidos
from src.etl.anonymize import anonimizar
from src.etl.load import guardar_csv, cargar_a_bd

logger = obtener_logger("etl.pipeline")

RUTA_ENTRADA = "data/input"
RUTA_SALIDA = "data/output"
RUTA_ERRORES = "data/errors"

def ejecutar_pipeline(uri_bd=None):
    archivos = listar_csv(RUTA_ENTRADA)

    if not archivos:
        logger.warning("No hay archivos para procesar")
        return

    for archivo in archivos:
        nombre = archivo.name

        logger.info(f"Procesando: {nombre}")

        try:
            df = leer_csv(archivo)
            df = limpiar(df)

            #CLIENTES
            if nombre.startswith("Clientes"):
                df_validos, df_invalidos = separar_validos_invalidos(df)
                df_validos = anonimizar(df_validos)

                guardar_csv(df_validos, f"{RUTA_SALIDA}/{nombre}")
                guardar_csv(df_invalidos, f"{RUTA_ERRORES}/{nombre}")

                if uri_bd:
                    cargar_a_bd(df_validos, "clientes", uri_bd)

            #TARJETAS
            elif nombre.startswith("Tarjetas"):
                df = anonimizar(df)

                guardar_csv(df, f"{RUTA_SALIDA}/{nombre}")

                if uri_bd:
                    cargar_a_bd(df, "tarjetas", uri_bd)

            #OTROS ARCHIVOS
            else:
                logger.warning(f"Archivo ignorado: {nombre}")

            logger.info(f"Procesado correctamente: {nombre}")

        except Exception as e:
            logger.exception(f"Error procesando {archivo}: {e}")
