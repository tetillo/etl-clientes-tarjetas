import re

def enmascarar_tarjeta(tarjeta):
    if not isinstance(tarjeta, str):
        return ""

    digitos = re.sub(r"\D", "", tarjeta)

    if len(digitos) < 4:
        return "****"

    return "*" * (len(digitos) - 4) + digitos[-4:]


def enmascarar_cvv(cvv):
    return "***"


def anonimizar(df):
    df = df.copy()

    if "tarjeta" in df.columns:
        df["tarjeta"] = df["tarjeta"].apply(enmascarar_tarjeta)

    if "cvv" in df.columns:
        df["cvv"] = df["cvv"].apply(enmascarar_cvv)

    return df