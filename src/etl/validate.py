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

    df["dni_ok"] = df["dni"].apply(lambda x: "Y" if validar_dni(x) else "N")
    df["dni_ko"] = df["dni"].apply(lambda x: "N" if validar_dni(x) else "Y")

    df["correo_ok"] = df["correo"].apply(lambda x: "Y" if validar_email(x) else "N")
    df["correo_ko"] = df["correo"].apply(lambda x: "N" if validar_email(x) else "Y")

    df["telefono_ok"] = df["telefono"].apply(lambda x: "Y" if validar_telefono(x) else "N")
    df["telefono_ko"] = df["telefono"].apply(lambda x: "N" if validar_telefono(x) else "Y")


    mascara = (
        (df["dni_ok"] == "Y") &
        (df["correo_ok"] == "Y") &
        (df["telefono_ok"] == "Y")
    )

    df_validos = df[mascara].copy()
    df_invalidos = df[~mascara].copy()

    return df_validos, df_invalidos