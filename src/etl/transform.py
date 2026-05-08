def limpiar(df):
    df = df.copy()

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

    if "cod_cliente" in df.columns:
        df["cod_cliente"] = df["cod_cliente"].str.upper().str.strip()

    df = df.drop_duplicates()

    return df