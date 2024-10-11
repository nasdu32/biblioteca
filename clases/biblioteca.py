from miembro import Miembro
from libro import Libro

class Biblioteca:
    def init(self, nombre, libros):
        
        self._nombre = nombre
        self._libros = libros
        self._personas = []

    def agregar_persona(self, persona):
        self._personas.append(persona)

    def buscar_libro(self, titulo):
        
        return next((libro for libro in self._libros if libro.titulo == titulo), None)

    def prestar_libro(self, titulo, id_miembro):
        
        libro = self.buscar_libro(titulo)
        miembro = next((p for p in self._personas if isinstance(p, Miembro) and p._id == id_miembro), None)
        if libro and miembro:
            return miembro.prestar_libro(libro)
        return False

    def devolver_libro(self, titulo, id_miembro):
        
        libro = self.buscar_libro(titulo)
        miembro = next((p for p in self._personas if isinstance(p, Miembro) and p._id == id_miembro), None)
        if libro and miembro:
            return miembro.devolver_libro(libro)
        return False