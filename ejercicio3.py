from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    @abstractmethod
    def es_valida(self, password: str) -> bool:
        pass

class ReglaLongitudMinima(ReglaValidacion):
    def es_valida(self, password: str) -> bool:
        return len(password) >= 8

class ReglaContieneNumero(ReglaValidacion):
    def es_valida(self, password: str) -> bool:
        return any(caracter.isdigit() for caracter in password)

class ReglaContieneMayuscula(ReglaValidacion):
    """Otra subclase que puede sustituir a cualquier regla en la colección."""

    def es_valida(self, password: str) -> bool:
        return any(caracter.isupper() for caracter in password)

# --- Pruebas TDD (Ejecutable) ---
if __name__ == "__main__":
    reglas: list[ReglaValidacion] = [
        ReglaLongitudMinima(),
        ReglaContieneNumero(),
        ReglaContieneMayuscula()
    ]

    # Comprobamos sustitución probando una contraseña que cumple todas las reglas
    password_valida = "Clave1234"
    assert all(r.es_valida(password_valida) for r in reglas) == True

    print("Ejercicio 3 (LSP) - ¡Todas las pruebas pasaron exitosamente!")