#Deicel Fernandez
print("Hecho por Deicel Fernandez.")


print("Ejercicio 1: Mayor de edad")

#Escribe un programa que le pida al usuario su edad y determine si es mayor de edad o no. Considera que la mayoría de edad se alcanza a los 18 años

edad = int(input("Ingresa tu edad: "))
if edad >= 18 and edad < 98:
    print("Felicidades eres mayor de edad")
elif edad < 18 and edad > 0:
    print("Eres menor de edad")
elif  edad >= 98 or edad <= 0:
    print(f"{edad} no es una edad válida")


print("Ejercicio 2: Par o impar")

#Crea un programa que solicite al usuario un número entero y determine si es par o impar.

num = int(input("Ingresa un numero: "))
if num % 2 == 0:
    print(f"{num} es un numero par")
else:
    print(f"{num} es un numero impar")


print("Ejercicio 3: Comparar dos números")

#Desarrolla un programa que pida al usuario dos números y muestre cuál de los dos es mayor, o si son iguales.

numero1 = int(input("Escriba el primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} es mayor que {numero1}")
elif numero1 == numero2:
    print(" Ambos numeros son iguales")

print("Ejercicio 4: Verificar si el año es bisiesto")

#Escribe un programa que solicite un año y verifique si es un año bisiesto. Un año es bisiesto si es divisible por 4, excepto los años que son divisibles por 100 pero no por 400.

num = int(input("Digite el año: "))
if num % 4 != 0:
    print(f"{num} no es un año bisiesto ")
elif num % 4 == 0 and num % 100 != 0:
    print(f"{num} es un año bisiesto ")
elif num % 4 == 0 and num % 100 == 0 and num % 400 != 0:
    print(f"{num} no es un año bisiesto ")
elif num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
    print(f"{num} es un año bisiesto ")

print("Ejercicio 5: Calcular el descuento en una compra")

#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento. El programa debe pedir el monto original de la compra y el porcentaje de descuento a aplicar.

precio_o = int(input("Digite el precio original: "))
descuento = int(input("Digite el descuento a aplicar: "))

precio_desp_desc = precio_o - ((descuento / 100) * precio_o) 
print(f"Despues de aplicar el {descuento}% de descuento a {precio_o}, el precio queda: {precio_desp_desc}")


print("Ejercicio 6: Operaciones aritméticas básicas")

#Desarrolla un programa que pida dos números y realice las cuatro operaciones aritméticas básicas con ellos: suma, resta, multiplicación y división. Debe mostrar los resultados de cada operación.

num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multip = num1 * num2
division = num1 / num2
print(f"El resultado de todas las operaciones es el siguiente:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multip}")
print(f"Division:{division}")


print("Ejercicio 7: Número dentro de un rango")

#Escribe un programa que verifique si un número ingresado por el usuario se encuentra dentro de un rango específico (por ejemplo, entre 10 y 50). Deberás solicitar el número y luego indicar si está o no dentro del rango.

number1 = int(input("Ingrese el numero: "))
if number1 >= 30 and number1 <= 80:
    print("Su numero de encuentra dentro del rango")
else:
    print("Su numero no se encuentra dentro del rango")


print("Ejercicio 8: Información del usuario")

#Crea un programa que pida al usuario su nombre, edad y ciudad de residencia. Al final, debe mostrar un mensaje con toda la información ingresada, por ejemplo: "Nombre: [nombre], Edad: [edad], Ciudad: [ciudad]".

nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
ciudad = input("Escriba su ciudad de origen: ")

print(f"Su nombre es: {nombre}")
print(f"Su edad es: {edad}")
print(f"Su ciudad de origen es: {ciudad}")


print("Ejercicio 9: Suma de dos números")

#Escribe un programa que pida al usuario dos números y muestre el resultado de su suma.

number_one = int(input("Dime un numero: "))
number_two = int(input("Dime otro numero: "))

suma1 = number_one + number_two
print(f"El resultado de la suma es: {suma1}")


print("Ejercicio 10: Comparación de dos números con operadores lógicos")

#Desarrolla un programa que solicite dos números y utilice operadores lógicos para verificar si ambos números son mayores que 10. El programa debe imprimir True si se cumple la condición y False en caso contrario.

numer1 = int(input("Digite un numero: "))
numer2 = int(input("Digite otro numero"))
resultado1 = (numer1 and numer2 > 10)

if resultado1 == True:
    print(f"Ambos numeros son mayores a 10?:{resultado1}")
else:
    print(f"Ambos numeros son mayores a 10?:{resultado1}")


print("Ejercicio 11: Comparación de tres números con operadores lógicos")

#Crea un programa que pida tres números y determine si el primero es mayor que el segundo y si el segundo es mayor que el tercero.

digito1 = int(input("Digite el primer numero: "))
digito2 = int(input("Digite el segundo numero: "))
digito3 = int(input("Digite el tercer numero: "))

if digito1 > digito2 and digito2 > digito3:
    print(f"{digito1} es mayor que {digito2} y {digito2} es mayor que {digito3}")
elif digito1 > digito2 and digito2 < digito3:
    print(f"{digito1} es mayor que {digito2} y {digito2} no es mayor que {digito3}")
elif digito1 < digito2 and digito2 > digito3:
    print(f"{digito1} no es mayor que {digito2} y {digito2} es mayor que {digito3}")
else:
    print(f"{digito1} no es mayor que {digito2} y {digito2} tampoco es mayor que {digito3}")
    
    
print("Ejercicio 12: Operadores lógicos (and, or, not)")

#Escribe un programa que demuestre el uso de los operadores lógicos and, or y not. Puedes crear dos variables booleanas con valores predefinidos (True o False) y mostrar el resultado de aplicar estos operadores.

opcion1 = int(input("Escribe un numero: "))
opcion2 = int(input("Escribe otro numero: "))


and_condition = (opcion1 > opcion2 and opcion2 < opcion1)  
or_condition = (opcion1 > opcion2 or opcion2 > opcion1)
not_condition = not (opcion1 > opcion2)

print(f"And: {and_condition}, Or: {or_condition}, Not: {not_condition}")


print("Ejercicio 13: Combinación de operadores lógicos y relacionales")

#Desarrolla un programa que pida un número al usuario y determine si dicho número es par y si se encuentra en el rango de 20 a 50.

numberr1 = int(input("Dime un numero: "))
if numberr1 % 2 == 0 and numberr1 >= 20 and numberr1 <= 50:
    print(f"{numberr1} es un numero par y esta dentro del rango establecido")
elif numberr1 % 2 == 0 and numberr1 < 20 or numberr1 > 50:
    print(f"{numberr1} es un numero par y no esta dentro del rango establecido")
elif numberr1 % 2 !=0 and numberr1 < 20 or numberr1 > 50:
    print(f"{numberr1} es un numero impar y no esta dentro del rango establecido")
elif numberr1 % 2 != 0 and numberr1 >= 20 and numberr1 <= 50:
    print(f"{numberr1} es un numero impar y esta dentro del rango establecido")


print("Ejercicio 14: Calificación por nota")

#Crea un programa que pida una calificación numérica del 1 al 100 y la convierta a una calificación alfabética, según la siguiente escala:

#90-100: A

#80-89: B

#70-79: C

#60-69: D

#Menos de 60: F

puntuacion = int(input("Escriba su nota: "))
if puntuacion >= 90 and puntuacion <=100:
    print("Obtuviste una A")
elif puntuacion >= 80 and puntuacion <= 89:
    print("Obtuviste una B")
elif puntuacion >= 70 and puntuacion <= 79:
    print("Obtuviste una C")
elif puntuacion >= 60 and puntuacion <= 69:
    print("Obtuviste una D")
elif puntuacion < 60:
    print("Obtuviste una F. Necesitas mejorar.")


print("Ejercicio 15: Determinar si un número es positivo, negativo o cero")

#Escribe un programa que solicite un número y determine si es positivo, negativo o igual a cero.

number = int(input("Ingrese un numero: "))
if number == 0:
    print("Tu numero es igual a cero")
elif number > 0:
    print("El numero es positivo")
else:
    print("Tu numero es negativo")



