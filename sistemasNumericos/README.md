# Conversor Entre Sistemas Numericos

## Descripción

Después de haber recordado las fórmulas para la conversión de números entre distintas bases
y como actividad en la clase de Electrónica Digital, se creó este programa para convertir
con facilidad entre sistemas y poner conocimientos de programación en práctica.

## Tecnologías

- Python
- CustomTkinter (Libreria)

## Funciones

La lógica de conversión es la misma en todas: si el número es 0 regresa `"0"` directo,
de lo contrario entra en un `while` que divide y acumula residuos hasta llegar a cero.

### `decimal_a_binario()`

Divide entre **2** en cada iteración. El residuo siempre es `1` o `0`, se convierte a string y se concatena al inicio de la variable `binario`, formando el número de derecha a izquierda. 

Despues la variable `decimal` toma el cociente entero y vuelve a repetir el proceso 

```python
binario = str(decimal % 2) + binario
decimal //= 2
```

### `decimal_a_octal()`

Mismo proceso, pero la división es entre **8**, por lo que los residuos van del `0` al `7`.

```python
octal = str(decimal % 8) + octal
decimal //= 8
```

### `decimal_a_hexadecimal()`

La diferencia aquí es que los residuos pueden ir del `0` al `15`. Del `0` al `9` se manejan igual, pero del `10` al `15` se convierten a letras (`A`-`F`) usando una funcion de python `chr()`.

```python
residuo = decimal % 16
if residuo < 10:
    hexadecimal = str(residuo) + hexadecimal
else:
    hexadecimal = chr(residuo - 10 + ord('A')) + hexadecimal
decimal //= 16
```

### `convertir()`

Es la función que conecta la interfaz con las anteriores. Toma el valor del campo de entrada, valida que sea un entero positivo, y según el botón que se presionó llama a la conversión correspondiente. Si el input no es válido muestra un mensaje de error.

```python
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

```