class FiguraGeometrica:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # ENCAPSULAMIENTO
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self.__ancho = valor

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self.__alto = valor

    def area(self):
        return self.__ancho * self.__alto

    def perimetro(self):
        raise NotImplementedError(
            "El método perímetro debe implementarse"
        )

    def __str__(self):
        return (
            f"Ancho: {self.__ancho}, "
            f"Alto: {self.__alto}"
        )
