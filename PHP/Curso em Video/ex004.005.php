<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<div>
    <?php
        $n1 = 5;
        $n2 = 26;
        $s = $n1 + $n2;
        echo "A soma entre $n1 e $n2 e igual a $s";
    ?>
</div>
<div>
    <?php
        $n1 = $_GET["a"];
        $n2 = $_GET["b"];
        echo "<h1>Valores Recebidos: $n1 e $n2</h1>";
        $m = ($n1 + $n2) / 2;
        echo "<br/>A soma vale ".($n1+$n2);
        echo "<br/>A subtração vale ".($n1-$n2);
        echo "<br/>A Multiplicação vale ".($n1*$n2);
        echo "<br/>A Divisão vale ".($n1/$n2);
        echo "<br/>O Modulo vale ".($n1%$n2);
        echo "<br/>A Media Vale $m";
    ?>
</div>

</div>
</body>
</html