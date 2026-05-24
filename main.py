from cuadrado import Cuadrado
from rectangulo import Rectangulo


def sumar_areas(figuras):
    total = 0

    for figura in figuras:
        total += figura.area()

    return total


def sumar_perimetros(figuras):
    total = 0

    for figura in figuras:
        total += figura.perimetro()

    return total


print("=== CREANDO FIGURAS ===")

cuadrado1 = Cuadrado(5)
cuadrado2 = Cuadrado(8)

rectangulo1 = Rectangulo(4, 7)
rectangulo2 = Rectangulo(6, 3)

figuras = [
    cuadrado1,
    cuadrado2,
    rectangulo1,
    rectangulo2
]

print("\n=== DATOS DE LAS FIGURAS ===")

for figura in figuras:
    print(figura)
    print(f"Área: {figura.area()}")
    print(f"Perímetro: {figura.perimetro()}")
    print("--------------------")

print("\n=== SUMAS TOTALES ===")

print(f"Suma áreas: {sumar_areas(figuras)}")
print(f"Suma perímetros: {sumar_perimetros(figuras)}")

print("\n=== VALIDACIONES ===")

try:
    cuadrado_error = Cuadrado(-5)

except ValueError as error:
    print(f"Error detectado: {error}")

try:
    rectangulo_error = Rectangulo(0, 4)

except ValueError as error:
    print(f"Error detectado: {error}")

print("\n=== MODIFICANDO VALORES ===")

rectangulo1.ancho = 10
rectangulo1.alto = 20

print(rectangulo1)
print(f"Área nueva: {rectangulo1.area()}")
print(f"Perímetro nuevo: {rectangulo1.perimetro()}")