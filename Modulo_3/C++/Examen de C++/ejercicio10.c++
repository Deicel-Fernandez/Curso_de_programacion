////🧮 Ejercicio 10: Constantes const y Funciones void
////Crea un programa para calcular el perímetro de un círculo.
////- Declara una constante de tipo double usando la palabra clave const para el valor de Pi (π≈3.14159).
////- Escribe una función void llamada calcularPerimetro que no devuelva ningún valor 
////pero que reciba como parámetro el radio del círculo.
////- Dentro de esta función, calcula el perímetro (2⋅π⋅radio) y muéstralo directamente en la consola.
////- Desde main, pide al usuario el radio y llama a la función calcularPerimetro.

#include <iostream>

const double PI = 3.14159;

void calcularPerimetro(double rad) {
    double perim = 2 * PI * rad;
    std::cout << "El perimetro del circulo es: " << perim << std::endl;
}

int main() {
    double radU;

    std::cout << "Ingrese el radio del circulo: ";
    std::cin >> radU;

    calcularPerimetro(radU);

    return 0;
}





