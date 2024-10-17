from errores import ValidacionGanimedesError, ValidacionCalistoError

class ReglaValidacion:
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) <= self._longitud_esperada:
            raise NotImplementedError()

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)
    
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        return any(c in '@_#$%' for c in clave)

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        if not self._contiene_mayuscula(clave):
            raise ValidacionGanimedesError("La clave debe tener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise ValidacionGanimedesError("La clave debe tener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise ValidacionGanimedesError("La clave debe tener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise ValidacionGanimedesError("La clave debe tener al menos un caracter especial (@, _, #, $, %)")
        return True