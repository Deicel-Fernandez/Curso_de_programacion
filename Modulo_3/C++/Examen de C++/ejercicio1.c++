//🧪 Ejercicio 1: "Hola Mundo" y Tipos de Datos
//Escribe un programa que imprima en la consola el mensaje "¡Hola, Mundo!". 
// Luego, declara e inicializa una variable para cada uno de los siguientes tipos de datos:
//- Entero (int)
//- Flotante (float)
//- Carácter (char)
//- Booleano (bool)

#include <iostream> 
#include <string>   

int main() {
    
    std::cout << "¡Hola, Mundo!" << std::endl;

    int edad = 30;
    std::cout << "Mi edad es: " << edad << std::endl;
   
    float precio = 19.99f; 

    char inicial = 'D'; 
    std::cout << "Mi inicial es: " << inicial << std::endl;

    bool esEstudiante = true;  
    std::cout << "¿Soy estudiante?: " << esEstudiante << std::endl; 

    bool soyMayorDeEdad = false;
    std::cout << "¿Soy mayor de edad?: " << soyMayorDeEdad << std::endl; 
    
    return 0;
 }









