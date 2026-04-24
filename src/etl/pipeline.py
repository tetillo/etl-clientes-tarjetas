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
        logger.info(f"Procesando: {archivo}")

        try:
            df = leer_csv(archivo)
            df = limpiar(df)

            df_validos, df_invalidos = separar_validos_invalidos(df)
            df_validos = anonimizar(df_validos)

            guardar_csv(df_validos, f"{RUTA_SALIDA}/{archivo.name}")
            guardar_csv(df_invalidos, f"{RUTA_ERRORES}/{archivo.name}")

            if uri_bd:
                cargar_a_bd(df_validos, "clientes", uri_bd)

            logger.info(f"Procesado correctamente: {archivo.name}")

        except Exception as e:
            logger.exception(f"Error procesando {archivo}: {e}")