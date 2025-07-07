print("Hola")

#Imprimir una sumaaaaaaaaa
a = 10
b = 20
suma = a + b
print(suma) 

#Imprimir un mensaje
saludo = "Hola, "
nombre = "Deicel"
mensaje = saludo + nombre
print(mensaje)

#Imprimir edad
edad = 17
es_adulto = edad > 18
print(es_adulto)

# Operadores aritmeticos

c = 20
d = 15
suma = c + d
resta = c + d
multiplicacion = c + d
division = c + d
division_entera = c + d
modulo = c % d
exponente = c + d
print(division)

# Operadores logicos
# Not, and i or

# Not para negar
# And si ambas son verdaderas=False
# Or si una es verdadera=True

#Ejercicio 1

mensaje_1 = "Mi nombre es: "
nombre_1 = "Deicel"
mensaje_2 = ", tengo "
edad_1 = "18"
mensaje_3 = " años y vivo en "
ciudad_1 = "Maracaibo"
resultado = mensaje_1 + nombre_1 + mensaje_2 + edad_1 + mensaje_3 + ciudad_1
print(resultado)

#Ejercicio 2

e = 13
f = 17
g = 20

suma = e + f + g
division = suma / 3
print(division)

formulario = input("Dime tu nombre: ")
print(f"Tu nombre es: {formulario}")
formulario_numero = int (input("Cual es tu edad: "))
print(f"Tu edad es: {formulario_numero}")

Calcular = 20
Resultado = formulario_numero + Calcular
print(Resultado)

A = 12
modulo = A % 2
print(modulo)



#Condicionales

# If, Elif y Else

puntuacion = 78
if puntuacion >= 90-100:
    print("Obtuviste una A")
elif puntuacion >= 80-89:
    print("Obtuviste una B")
elif puntuacion >= 70-79:
    print("Obtuviste una C")
elif puntuacion >= 60-69:
    print("Obtuviste una F")
elif puntuacion >= 0-59:
    print("Obtuviste una F")
else:
    print("Necesitas mejorar.")