////📋 Ejercicio 6: Bucle do-while y switch
////Escribe un programa que muestre un menú simple con tres opciones:
////1. Saludar
////2. Despedirse
////3. Salir

#include <iostream>

int main() {
    int opcion;

    do {
      
        std::cout << "\nBienvenido" << std::endl;
        std::cout << "1. Saludar" << std::endl;
        std::cout << "2. Despedirse" << std::endl;
        std::cout << "3. Salir" << std::endl;
        std::cout << "Elige una opción: ";
        std::cin >> opcion;

        switch (opcion) {
            case 1:
                std::cout << "Helou" << std::endl;
                break;
            case 2:
                std::cout << "Ciao pue" << std::endl;
                break; 
            case 3:
                std::cout << "Te fuiste, ciao" << std::endl;
                break;
            default:
                std::cout << "No seleccionaste una opcion valida , elige una opción del 1 al 3" << std::endl;
                break;
        }
    } while (opcion != 3);

    return 0;
}