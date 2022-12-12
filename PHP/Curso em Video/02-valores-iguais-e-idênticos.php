<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php 
    $a = 3;
    $b = "3";
    echo "<br> Valores recebidos $a e $b <br>";
    $r = ($a == $b)?"sim":"não";
    echo " <br> As variaveis A e B são iguais? $r <br>";

    $a = 3;
    $b = "3";
    $r = ($a === $b)?"sim":"não";
    echo "<br> As variaveis A e B são identicas? $r";
?>
</body>
</html>