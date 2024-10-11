from persona import Persona

class Bibliotecario(Persona):
    def init(self, nombre, id, turno):
        super().init(nombre, id)
        self._turno = turno

    def agregar_libro(self, biblioteca, libro):
        biblioteca._libros.append(libro)

    def eliminar_libro(self, biblioteca, titulo):
        biblioteca._libros = [lib for lib in biblioteca._libros if lib.titulo != titulo]

    def informacion(self):
        return super().informacion() + f", Tipo: Bibliotecario, Turno: {self._turno}"