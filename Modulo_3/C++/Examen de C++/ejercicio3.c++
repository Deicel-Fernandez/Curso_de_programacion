//🔍 Ejercicio 3: Condicionales if-else
//Desarrolla un programa que pida al usuario su edad.
// El programa debe utilizar una estructura condicional if-else para determinar 
// si el usuario es mayor de edad (18 años o más) y mostrar un mensaje apropiado en la pantalla.

#include <iostream>

int main() {
    int edad;

    std::cout << "Introduce tu edad: ";
    std::cin >> edad;

    if (edad >= 18){
        std::cout << "Eres mayor de edad" << std::endl;
    } else {
        std::cout <<"Eres menor de edad" << std::endl;
    }

    return 0;
}