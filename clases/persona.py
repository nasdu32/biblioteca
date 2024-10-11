class Persona:
    def init(self, nombre, id):
        self._nombre = nombre
        self._id = id

    def informacion(self):
        return f"Nombre: {self._nombre}, ID: {self._id}"