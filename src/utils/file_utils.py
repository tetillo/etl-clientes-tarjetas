from pathlib import Path

def listar_csv(ruta):
    return list(Path(ruta).glob("*.csv"))