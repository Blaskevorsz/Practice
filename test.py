# Define la interfaz de la expresión
class ExpresionBinaria:
    def interpretar(self):
        pass

# Implementa las expresiones terminales
class NumeroDecimal(ExpresionBinaria):
    def __init__(self, numero):
        # Llama al constructor de la clase base
        self.numero = numero

    def interpretar(self):
        return bin(self.numero)[2:]  # Convierte el número decimal a binario

# Crea un contexto (opcional)
class ContextoConversion:
    def __init__(self):
        self.resultado = ""

# Uso del intérprete
contexto = ContextoConversion()

expresion = NumeroDecimal(10)
contexto.resultado = expresion.interpretar()
print("Representación binaria de 10:", contexto.resultado)  # Esto imprimirá "Representación binaria de 10: 1010"

expresion = NumeroDecimal(23)
contexto.resultado = expresion.interpretar()
print("Representación binaria de 23:", contexto.resultado)  # Esto imprimirá "Representación binaria de 23: 10111"
