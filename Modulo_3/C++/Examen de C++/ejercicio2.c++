#include <iostream> 
#include <cmath>    
#include <iomanip>  

int main() {
    double num1, num2;

    std::cout << "Ingresa el primer numero: ";
    std::cin >> num1;

    std::cout << "Ingresa el segundo numero: ";
    std::cin >> num2;

    std::cout << "\n--- Operaciones Basicas ---\n";
    std::cout << "Suma: " << num1 + num2 << std::endl;
    std::cout << "Resta: " << num1 - num2 << std::endl;
    std::cout << "Multiplicacion: " << num1 * num2 << std::endl;

    //basicas
    if (num2 != 0) {
        std::cout << "Division: " << num1 / num2 << std::endl;
    } else {
        std::cout << "Division: No se puede dividir por cero." << std::endl;
    }
     std::cout << "\n--- Resultados con <cmath> ---\n";

    ///cmath
    std::cout << "Potencia (" << num1 << "^" << num2 << "): " << std::pow(num1, num2) << std::endl;

    if (num1 >= 0) {
        std::cout << "Raiz cuadrada de " << num1 << ": " << std::sqrt(num1) << std::endl;
    } else {
        std::cout << "Raiz cuadrada de " << num1 << ": No se puede calcular la raiz cuadrada de un numero negativo." << std::endl;
    }
    
    return 0;
}   