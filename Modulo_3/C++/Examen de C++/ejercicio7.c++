////📐 Ejercicio 7: Funciones con Valor de Retorno
////Desarrolla un programa que contenga una función llamada calcularAreaRectangulo.
////- Declara (Prototipo) la función al inicio del programa.
////- La función debe recibir dos parámetros de tipo float: la base y la altura.
////- La función debe devolver el área calculada.
////- Desde la función main, solicita al usuario la base y la altura, llama a la función y muestra el resultado.

#include <iostream>

float calcularAreaRectangulo(float base, float altura);

int main() {
    float base;
    float altura;

    std::cout << "Decime la base del rectangulo: ";
    std::cin >> base;

    std::cout << "Decime la altura del rectangulo: ";
    std::cin >> altura;

    float area = calcularAreaRectangulo(base altura);

    std::cout << "El area del rectangulo es: " << area << std::endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura; 
}


