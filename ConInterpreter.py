
class ExpresionBinaria:
    def interpretar(self):
        pass


class NumeroDecimal(ExpresionBinaria):
    def __init__(self, numero):
        # Llama al constructor de la clase base
        self.numero = numero

    def interpretar(self):
        return bin(self.numero)[2:]  


class ContextoConversion:
    def __init__(self):
        self.resultado = ""

contexto = ContextoConversion()

expresion = NumeroDecimal(10)
contexto.resultado = expresion.interpretar()
print("Representación binaria de 10:", contexto.resultado) 

expresion = NumeroDecimal(23)
contexto.resultado = expresion.interpretar()
print("Representación binaria de 23:", contexto.resultado)  
