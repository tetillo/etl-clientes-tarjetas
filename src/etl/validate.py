import re

LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"

def validar_dni(dni):
    if not isinstance(dni, str):
        return False

    dni = dni.strip().upper()

    if not re.match(r"^\d{8}[A-Z]$", dni):
        return False

    return LETRAS_DNI[int(dni[:-1]) % 23] == dni[-1]


def validar_email(email):
    if not isinstance(email, str):
        return False
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


def validar_telefono(telefono):
    if not isinstance(telefono, str):
        return False

    telefono = re.sub(r"\s+", "", telefono)
    return re.match(r"^[6789]\d{8}$", telefono) is not None


def separar_validos_invalidos(df):
    df = df.copy()

    df["dni_valido"] = df["dni"].apply(validar_dni)
    df["email_valido"] = df["email"].apply(validar_email)
    df["telefono_valido"] = df["telefono"].apply(validar_telefono)

    mascara = (
        df["dni_valido"] &
        df["email_valido"] &
        df["telefono_valido"]
    )

    df_validos = df[mascara].copy()
    df_invalidos = df[~mascara].copy()

    return df_validos, df_invalidos