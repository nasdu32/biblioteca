class Libro:
    def init(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponible = True

    @property
    def titulo(self):
        return self._titulo

    def esta_disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        self._disponible = estado