from trasformacion.binario_to_decimal import BinarioADecimal

if __name__ == "__main__":
    binario = input("Introduce un número binario: ")
    if not all(c in '01' for c in binario):
        print("Error: Por favor, ingrese un número binario válido.")
        while True:
            try:
                int(binario, 2)
                break
            except ValueError:
                binario = input("Entrada inválida. Introduce un número binario: ")

    conversor = BinarioADecimal(binario)
    decimal = conversor.convertir()
    print("El número entero:", decimal)



"""
#Metodo simple sin clases
binario = input("Introduce un número binario: ")
decimal = 0
potencia = 0

for digito in reversed(binario):
    decimal += int(digito) * (2 ** potencia)
    potencia += 1

print("El número decimal es:", decimal)
"""
