///🔁 Ejercicio 4: Bucle for y Constantes con #define
///Utiliza #define para crear una constante simbólica llamada LIMITE con un valor de 10. 
///Luego, escribe un programa que pida al usuario un número y utilice un bucle for para imprimir la tabla de multiplicar de ese número desde 1 hasta LIMITE.

#include <iostream> 

#define LIMITE 10

int main() {
    int numero;

    std::cout << "Ingresa un numero: ";
    std::cin >> numero;
    std::cout << "\n--- Tabla de Multiplicar del " << numero << " ---\n";

    for (int i = 1; i <= LIMITE; ++i) {
        std::cout << numero << " x " << i << " = " << (numero * i) << std::endl;
    }

    return 0; 
}