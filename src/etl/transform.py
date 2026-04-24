def limpiar(df):
    df = df.copy()

    df.columns = [c.strip().lower() for c in df.columns]

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

    df = df.drop_duplicates()

    return df