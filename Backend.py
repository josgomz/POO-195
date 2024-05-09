class backend:
    def CadenaCaracter(self, dato):
        index = dato
        nombres = ["Leo", "Aldo", "Luis", "Parra"]
        try:
            return nombres[index]
        except ValueError:
            dato = ValueError
            return dato