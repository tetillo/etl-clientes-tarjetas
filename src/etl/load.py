from pathlib import Path
from sqlalchemy import create_engine

def guardar_csv(df, ruta):
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(ruta, index=False)

def cargar_a_bd(df, nombre_tabla, uri_bd):
    try:
        engine = create_engine(uri_bd)

        df.to_sql(
            nombre_tabla,
            engine,
            if_exists="append",
            index=False,
            method="multi"  # inserta más rápido
        )

        print(f" Insertados en {nombre_tabla}")

    except Exception as e:
        print(f" Error BD: {e}")
