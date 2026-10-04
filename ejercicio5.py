from abc import ABC, abstractmethod

# Abstracción
class ReglaValidacion(ABC):
    @abstractmethod
    def es_valida(self, password: str) -> bool:
        pass

# Módulos de bajo nivel (Reglas concretas)
class ReglaLongitudMinima(ReglaValidacion):
    def __init__(self, longitud: int = 8):
        self.longitud = longitud

    def es_valida(self, password: str) -> bool:
        return len(password) >= self.longitud

class ReglaContieneNumero(ReglaValidacion):
    def es_valida(self, password: str) -> bool:
        return any(caracter.isdigit() for caracter in password)

# Módulo de alto nivel con Inyección de Dependencias
class ValidadorPassword:
    def __init__(self, reglas: list[ReglaValidacion]):
        self.reglas = reglas  # Inyección por constructor

    def validar(self, password: str) -> bool:
        return all(regla.es_valida(password) for regla in self.reglas)


# --- Pruebas TDD Finales (Ejecutable) ---
if __name__ == "__main__":
    # Inyectamos las reglas desacopladas
    reglas = [ReglaLongitudMinima(8), ReglaContieneNumero()]
    validador = ValidadorPassword(reglas)

    # 1. Contraseña corta (debe ser False)[cite: 2]
    assert validador.validar("12345") == False

    # 2. Contraseña sin números (debe ser False)[cite: 2]
    assert validador.validar("abcdefgh") == False

    # 3. Contraseña correcta (debe ser True)[cite: 2]
    assert validador.validar("clave1234") == True

    print("Ejercicio 5 (DIP) - ¡Todas las pruebas del validador pasaron exitosamente!")