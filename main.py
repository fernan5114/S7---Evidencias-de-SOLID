class ReglaLongitudMinima:
    """Valida únicamente que la contraseña cumpla con la longitud requerida."""

    def __init__(self, longitud_minima: int = 8):
        self.longitud_minima = longitud_minima

    def es_valida(self, password: str) -> bool:
        return len(password) >= self.longitud_minima

# --- Pruebas TDD (Ejecutable) ---
if __name__ == "__main__":
    regla = ReglaLongitudMinima(8)

    # 1. Red -> Green -> Refactor
    assert regla.es_valida("12345") == False, "Prueba fallida: Contraseña corta"
    assert regla.es_valida("12345678") == True, "Prueba fallida: Longitud correcta"

    print("Ejercicio 1 (SRP) - ¡Todas las pruebas pasaron exitosamente!")