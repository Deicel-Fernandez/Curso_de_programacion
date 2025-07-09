////🍽️ Ejercicio 9: Librerías vector y string
////Escribe un programa que pida al usuario que ingrese 3 de sus comidas favoritas. 
////Almacena cada comida en un vector de tipo string. Después de que el usuario haya ingresado las tres, 
////utiliza un bucle para recorrer el vector e imprimir cada una de las comidas en la consola.

#include <iostream> // Necesario para operaciones de entrada/salida
#include <vector>   // Necesario para usar std::vector
#include <string>   // Necesario para usar std::string

int main() {
    std::vector<std::string> foodFav;
    std::string food;

    std::cout << "Haceme el favor, ingresa 3 de tus comidas favoritas" << std::endl;

    for (int i = 0; i < 3; ++i) {
        std::cout << "food #" << (i + 1) << ": ";
        std::getline(std::cin, food);
        fooodFav.push_back(food);
    }

    std::cout << "\nTus comidas favoritas son:" << std::endl;


    for (const std::string &item : foodFav) {
        std::cout << "- " << item << std::endl;
    }

    return 0;
}