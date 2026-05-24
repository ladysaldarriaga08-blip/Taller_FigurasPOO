# Taller Figuras Geométricas POO

## Descripción

Este proyecto fue desarrollado en Python aplicando los conceptos de Programación Orientada a Objetos (POO).

El taller consiste en implementar una jerarquía de clases para representar figuras geométricas utilizando:

- Encapsulamiento
- Herencia
- Polimorfismo
- Sobrescritura de métodos
- Validaciones internas
- Buenas prácticas PEP8

---

# Estructura del Proyecto

/TallerFigurasPOO/

│── figura_geometrica.py  
│── cuadrado.py  
│── rectangulo.py  
│── main.py  
└── README.md

---

# Explicación de las Clases

## FiguraGeometrica

Clase base del proyecto.

Contiene:

- atributos encapsulados:
  - ancho
  - alto
- validaciones con property y setter
- método area()
- método perimetro()
- método __str__()

---

## Cuadrado

Clase hija de FiguraGeometrica.

Características:

- recibe un solo lado
- calcula área
- calcula perímetro
- sobrescribe __str__()

---

## Rectangulo

Clase hija de FiguraGeometrica.

Características:

- recibe ancho y alto
- calcula área
- calcula perímetro
- sobrescribe __str__()

---

# Funcionalidades Implementadas

✔ Encapsulamiento  
✔ Herencia  
✔ Polimorfismo  
✔ Sobrescritura de métodos  
✔ Validaciones con ValueError  
✔ Funciones para sumar áreas y perímetros  
✔ Modificación de atributos mediante setters  

---

# Ejemplo de Ejecución

=== CREANDO FIGURAS ===

=== DATOS DE LAS FIGURAS ===

Cuadrado -> Lado: 5  
Área: 25  
Perímetro: 20  

Cuadrado -> Lado: 8  
Área: 64  
Perímetro: 32  

Rectángulo -> Ancho: 4, Alto: 7  
Área: 28  
Perímetro: 22  

Rectángulo -> Ancho: 6, Alto: 3  
Área: 18  
Perímetro: 18  

=== SUMAS TOTALES ===

Suma áreas: 135  
Suma perímetros: 92  

=== VALIDACIONES ===

Error detectado: El ancho debe ser mayor que 0  
Error detectado: El ancho debe ser mayor que 0  

=== MODIFICANDO VALORES ===

Rectángulo -> Ancho: 10, Alto: 20  
Área nueva: 200  
Perímetro nuevo: 60

---

# Autor

Nombre del estudiante: ___________________

Materia: Programación Orientada a Objetos

Fecha: ___________________