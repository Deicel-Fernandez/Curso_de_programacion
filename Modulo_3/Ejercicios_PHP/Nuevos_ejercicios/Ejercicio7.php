<?php
#Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero y muestre el resultado
$numero = -7;

if ($numero > 0) {
    echo "El número " . $numero . " es positivo.\n";
} elseif ($numero < 0) {
    echo "El número " . $numero . " es negativo.\n";
} else {
    echo "El número " . $numero . " es cero.\n";
}
?>