import re
import hashlib

def enmascarar_tarjeta(numero):
    if not isinstance(numero, str):
        return ""

    numero = re.sub(r"\D", "", numero)

    if len(numero) < 4:
        return "XXXX"

    return "XXXX-XXXX-XXXX-" + numero[-4:]


def hash_cvv(cvv):
    return hashlib.sha256(str(cvv).encode()).hexdigest()


def anonimizar(df):
    df = df.copy()

    # TARJETAS
    if "numero_tarjeta" in df.columns:
        df["numero_tarjeta_masked"] = df["numero_tarjeta"].apply(enmascarar_tarjeta)
        df.drop(columns=["numero_tarjeta"], inplace=True)

    if "cvv" in df.columns:
        df["cvv_hash"] = df["cvv"].apply(hash_cvv)
        df.drop(columns=["cvv"], inplace=True)

    return df