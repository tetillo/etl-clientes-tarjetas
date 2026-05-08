from src.etl.pipeline import ejecutar_pipeline

if __name__ == "__main__":
    URI = "mysql+pymysql://root:@localhost:3306/gestion_pagos"
    ejecutar_pipeline(URI)
