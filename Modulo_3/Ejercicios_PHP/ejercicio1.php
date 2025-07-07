<?php

$a = 10;
$b = 17;

echo "Suma: " . ($a + $b) . "\n" ;
echo "Resta: " . ($a - $b) . "\n" ;
echo "Multiplicacion: " . ($a * $b) . "\n" ;
echo "Division: " . ($a / $b) . "\n" ;
echo "Modulo: " . ($a % $b) . "\n" ;

echo "Llevais pan, queso, jamon y un jugo Frutsy de naranja\nTodo te hace 12$ o 1250Bs\n¿Como vais a pagar?\n";
$metodopago = "tarjeta";

switch ($metodopago) {
    case "efectivo":
        echo "¿Efectivo?. Ve que no tengo vuelto.\n";
        break;
    case "efectivo":
        echo "¿Pago movil?. Me enseñais el capture.\n";
        break;
    case "tarjeta":
        echo "Elegiste tarjeta. Pasame la tarjeta... Cedula... ¿Ahorro o corriente?... Clave.\n";
        break;
    case "zelle":
        echo 'Pagais por zelle. Aqui estan los datos, poneis "ND546FA3" en la descripcion y me enseñas el capture.\n';
        break;
    case "paypal":
        echo "¿PayPal? vos pagais la comision.\n";
        break;
    default:
    echo "Decime como vais a pagar, que se esta haciendo cola.\n";
        break;
}
?>