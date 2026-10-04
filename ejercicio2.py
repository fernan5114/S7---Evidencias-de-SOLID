from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    """Clase base abierta a extensión, cerrada a modificación."""

    @abstractmethod
    def es_valida(self, password: str) -> bool:
        pass

class ReglaLongitudMinima(ReglaValidacion):
    def __init__(self, longitud_minima: int = 8):
        self.longitud_minima = longitud_minima

    def es_valida(self, password: str) -> bool:
        return len(password) >= self.longitud_minima

class ReglaContieneNumero(ReglaValidacion):
    """Nueva regla agregada mediante extensión."""

    def es_valida(self, password: str) -> bool:
        return any(caracter.isdigit() for caracter in password)

# --- Pruebas TDD (Ejecutable) ---
if __name__ == "__main__":
    regla_num = ReglaContieneNumero()

    assert regla_num.es_valida("abcdefgh") == False, "Prueba fallida: Sin números"
    assert regla_num.es_valida("clave123") == True, "Prueba fallida: Con números"

    print("Ejercicio 2 (OCP) - ¡Todas las pruebas pasaron exitosamente!")