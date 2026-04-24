import pandas as pd
import chardet

def detectar_codificacion(ruta_archivo):
    with open(ruta_archivo, "rb") as f:
        muestra = f.read(10000)
    return chardet.detect(muestra)["encoding"] or "utf-8"

def leer_csv(ruta_archivo):
    encoding = detectar_codificacion(ruta_archivo)

    try:
        return pd.read_csv(ruta_archivo, encoding=encoding)
    except Exception:
        return pd.read_csv(
            ruta_archivo,
            encoding="latin-1",
            on_bad_lines="skip"
        )