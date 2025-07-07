<?php
#Utilizando bucles anidados, crea un script que dibuje un cuadrado de 5x5 en la terminal utilizando el carácter #.
$numero = 5;

echo "Cuadrado de " . $numero . "x" . $numero . ":\n";
for ($i = 0; $i < $numero; $i++) {
    for ($j = 0; $j < $numero; $j++) {
        echo "# ";
    }
    echo "\n";
}
?>