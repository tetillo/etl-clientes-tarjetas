import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def obtener_logger(nombre):
    Path("logs").mkdir(exist_ok=True)

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formato = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
        )

        archivo = RotatingFileHandler(
            "logs/etl.log",
            maxBytes=1_000_000,
            backupCount=3
        )
        archivo.setFormatter(formato)

        consola = logging.StreamHandler()
        consola.setFormatter(formato)

        logger.addHandler(archivo)
        logger.addHandler(consola)

    return logger