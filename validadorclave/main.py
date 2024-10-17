from validadorclave.modelo.validador import Validador
from validadorclave.modelo.errores import ValidadorError

def validar_clave(clave, reglas):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para la regla: {regla.__class__.__name__}")
        except ValidadorError() as e:
            print(f"Error: {regla.__class__.__name__}: {e}")