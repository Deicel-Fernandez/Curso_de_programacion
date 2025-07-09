///🎯 Ejercicio 5: Bucle while
///Crea un programa que simule un juego de adivinanza. 
// El programa debe generar un número secreto (por ejemplo, int numeroSecreto = 42;). 
// Luego, debe pedir al usuario que adivine el número. Utiliza un bucle while para que el programa siga pidiendo un número mientras el usuario no adivine el correcto. 
// Proporciona pistas como "más alto" o "más bajo".

#include <iostream> 

int main() {
    int numeroSecreto = 42;
    int intentoUsuario;

    std::cout << "¿Listo para jugar?" << std::endl;
    std::cout << "Estoy pensando en un número entre 1 y 100. Adivinalo pues" << std::endl;

    while (intentoUsuario != numeroSecreto) {
        std::cout << "Ingresa tu número: ";
        std::cin >> intentoUsuario;
        
        if (intentoUsuario < numeroSecreto) {
            std::cout << "Sube más tu numero" << std::endl;
        } else if (intentoUsuario > numeroSecreto) {
            std::cout << "Te pasaste" << std::endl;
        }
    }

    std::cout << "Lo adivinaste, eres un vergatario. El numero era: " << numeroSecreto << std::endl;

    return 0;
}