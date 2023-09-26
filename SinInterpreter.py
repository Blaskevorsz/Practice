
class NumeroDecimal:
    def __init__(self, numero):
        self.numero = numero
    
    def interpretar(self):
        return bin(self.numero)[2:]

numero_decimal = NumeroDecimal(10)

representacion_binaria = numero_decimal.interpretar()

print(representacion_binaria) 