<?php
////Escribe un programa que imprima los números del 1 al 30. Para los múltiplos de 3, debe imprimir "Mar" en su lugar. 
////Para los múltiplos de 5, debe imprimir "Tierra". Para los múltiplos de ambos (3 y 5), debe imprimir "MarTierra".
for ($i = 1; $i <= 30; $i++) {
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo "MarTierra\n";
    } elseif ($i % 3 == 0) {
        echo "Mar\n";
    } elseif ($i % 5 == 0) {
        echo "Tierra\n";
    } else {
        echo $i . "\n";
    }
}
?>