from persona import Persona

class Miembro(Persona):
    def init(self, nombre, id):
        super().init(nombre, id)
        self._historial_prestamos = []

    def prestar_libro(self, libro):
        if libro.esta_disponible():
            libro.cambiar_disponibilidad(False)
            self._historial_prestamos.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self._historial_prestamos:
            libro.cambiar_disponibilidad(True)
            self._historial_prestamos.remove(libro)
            return True
        return False

    def informacion(self):
        return super().informacion() + f", Tipo: Miembro, Libros prestados: {len(self._historial_prestamos)}"
    