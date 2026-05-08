import pandas as pd
import chardet

def detectar_codificacion(ruta_archivo):
    with open(ruta_archivo, "rb") as f:
        muestra = f.read(10000)
    return chardet.detect(muestra)["encoding"] or "utf-8"


def leer_csv(ruta_archivo):
    encoding = detectar_codificacion(ruta_archivo)

    try:
        return pd.read_csv(
            ruta_archivo,
            encoding=encoding,
            sep=";",     
            dtype=str
        )
    except Exception:
        return pd.read_csv(
            ruta_archivo,
            encoding="latin-1",
            sep=";",           
            dtype=str,
            on_bad_lines="skip"
        )