////🔄 Ejercicio 8: Paso por Valor vs. Paso por Referencia
////Crea un programa que demuestre la diferencia entre el paso por valor y el paso por referencia.
////- Define una función void llamada modificarPorValor que reciba un entero por valor y le sume 10 dentro de la función.
////- Define otra función void llamada modificarPorReferencia que reciba un entero por referencia y le sume 10.
////- En main, declara una variable entera llamada numero e inicialízala en 20. 
////Imprime su valor, llama a modificarPorValor, vuelve a imprimir numero. 
////Luego, llama a modificarPorReferencia y vuelve a imprimir el valor de numero para observar la diferencia.

#include <iostream>


void modificarPorValor(int num) {
    num += 10;
    std::cout << "Dentro de modificarPorValor (por valor): " << num << std::endl;
}

void modificarPorReferencia(int &numRef) {
    numRef += 10;
    std::cout << "Dentro de modificarPorReferencia (por referencia): " << numRef << std::endl;
}

int main() {
    int numero = 20;

    std::cout << "Valor inicial de numero: " << numero << std::endl;

    modificarPorValor(numero);
    std::cout << "Valor de numero despues de modificarPorValor: " << numero << std::endl;

    modificarPorReferencia(numero);
    std::cout << "Valor de numero despues de modificarPorReferencia: " << numero << std::endl;

    return 0;
}
