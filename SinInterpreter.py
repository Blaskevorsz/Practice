# Define la clase NumeroDecimal sin usar el patrón Interpreter
class NumeroDecimal:
    def __init__(self, numero):
        self.numero = numero
    
    def interpretar(self):
        # Convertir el número decimal a binario y devolverlo
        return bin(self.numero)[2:]

# Crear una instancia de NumeroDecimal
numero_decimal = NumeroDecimal(10)

# Llamar al método interpretar para obtener la representación binaria
representacion_binaria = numero_decimal.interpretar()

# Imprimir la representación binaria
print(representacion_binaria)  # Esto imprimirá "1010"