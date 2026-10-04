from abc import ABC, abstractmethod

class ValidadorSimple(ABC):
    @abstractmethod
    def es_valida(self, password: str) -> bool:
        pass

class ValidadorConDetalles(ABC):
    """Interfaz segregada para validadores que reportan la razón del fallo."""

    @abstractmethod
    def obtener_errores(self, password: str) -> list[str]:
        pass

class ValidadorPasswordDetallado(ValidadorSimple, ValidadorConDetalles):
    def es_valida(self, password: str) -> bool:
        return len(password) >= 8 and any(c.isdigit() for c in password)

    def obtener_errores(self, password: str) -> list[str]:
        errores = []
        if len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")
        if not any(c.isdigit() for c in password):
            errores.append("La contraseña debe contener al menos un número.")
        return errores

# --- Pruebas TDD (Ejecutable) ---
if __name__ == "__main__":
    validador = ValidadorPasswordDetallado()

    # Pruebas con reporte de errores
    errores_corta = validador.obtener_errores("123")
    assert len(errores_corta) == 2, "Debería reportar 2 errores"

    errores_correcta = validador.obtener_errores("clave1234")
    assert len(errores_correcta) == 0, "No debería haber errores"

    print("Ejercicio 4 (ISP) - ¡Todas las pruebas pasaron exitosamente!")