<?php
$temperatura = 18; // Cambia esta variable para probar diferentes temperaturas

if ($temperatura < 10) {
    echo "La temperatura de " . $temperatura . "°C indica que hace frio.\n";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "La temperatura de " . $temperatura . "°C indica que está templado.\n";
} else {
    echo "La temperatura de " . $temperatura . "°C indica que es caluroso.\n";
}
?>