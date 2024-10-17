from errores import *

class ReglaValidacion:
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError("La clave debe tener más de {} caracteres".format(self._longitud_esperada))

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)
    
    def validar(self, clave: str) -> bool:
        self._validar_longitud(clave)

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe tener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe tener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe tener al menos un número")
    
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        return any(c in '@_#$%' for c in clave)

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        super().validar(clave)
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe tener al menos un caracter especial (@, _, #, $, %)")
        return True
    
    
class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = sum(1 for c in clave if c in 'CALISTO')
        return 2 <= mayusculas < len('CALISTO')

    def es_valida(self, clave: str) -> bool:
        super().validar(clave)
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe tener al menos un número")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La palabra 'calisto' debe estar escrita con al menos dos letras en mayúscula")
        return True
    

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)