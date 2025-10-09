#Crea un programa que convierta los numeros binarios a decimales.
class BinarioADecimal:
    def __init__(self, binario):
        self.binario = binario

    def convertir(self):
        decimal = 0
        potencia = 0

        for digito in reversed(self.binario): # Recorre la cadena de derecha a izquierda
#En (2 ** potencia) se optiene el 2^0, 2^1, 2^2, etc, y en int(digito) se obtiene el valor del digito actual (0 o 1) y al final se suma al valor total de decimal.           
            decimal += int(digito) * (2 ** potencia)   
            #el * en el imedio trasforma el "1" a decimal 1.         
            potencia += 1 #Incrementa la potencia de 2 en cada iteración osea 2^0, 2^1, 2^2, etc.

        return decimal