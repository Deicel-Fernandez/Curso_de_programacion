<?php
#Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero y muestre el resultado.

$sumaImpares = 0;

for ($i = 1; $i <= 100; $i++) {
    if ($i % 2 != 0) {
        $sumaImpares += $i;
    }
}

echo "La suma de todos los números impares del 1 al 100 es: " . $sumaImpares . "\n";
?>