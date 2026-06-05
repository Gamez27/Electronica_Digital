import customtkinter as ctk

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""

    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2

    return binario


def decimal_a_octal(decimal):
    if decimal == 0:
        return "0"

    octal = ""

    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8

    return octal


def decimal_a_hexadecimal(decimal):
    if decimal == 0:
        return "0"

    hexadecimal = ""

    while decimal > 0:
        residuo = decimal % 16

        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            hexadecimal = chr(residuo - 10 + ord('A')) + hexadecimal

        decimal //= 16

    return hexadecimal


def convertir(tipo):
    try:
        numero = int(entrada.get())

        if numero < 0:
            resultado.configure(text="No se permiten negativos")
            return

        if tipo == "binario":
            resultado.configure(
                text=f"Resultado: {decimal_a_binario(numero)}"
            )

        elif tipo == "octal":
            resultado.configure(
                text=f"Resultado: {decimal_a_octal(numero)}"
            )

        elif tipo == "hexadecimal":
            resultado.configure(
                text=f"Resultado: {decimal_a_hexadecimal(numero)}"
            )

    except ValueError:
        resultado.configure(text="Ingrese un numero valido")


# Configuración visual
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Convertidor entre sistemas numericos")
app.geometry("500x350")

titulo = ctk.CTkLabel(
    app,
    text="Convertidor entre sistemas numericos",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)

# Botones
frame_botones = ctk.CTkFrame(app)
frame_botones.pack(pady=10)

btn_binario = ctk.CTkButton(
    frame_botones,
    text="Binario",
    command=lambda: convertir("binario")
)
btn_binario.pack(side="left", padx=10)

btn_octal = ctk.CTkButton(
    frame_botones,
    text="Octal",
    command=lambda: convertir("octal")
)
btn_octal.pack(side="left", padx=10)

btn_hex = ctk.CTkButton(
    frame_botones,
    text="Hexadecimal",
    command=lambda: convertir("hexadecimal")
)
btn_hex.pack(side="left", padx=10)

# Entrada
entrada = ctk.CTkEntry(
    app,
    placeholder_text="Ingrese un número decimal",
    width=250
)
entrada.pack(pady=20)

# Resultado
resultado = ctk.CTkLabel(
    app,
    text="Resultado:",
    font=("Arial", 16)
)
resultado.pack(pady=20)

app.mainloop()