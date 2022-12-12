<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


<?php
    $preco = $_GET["p"];
    echo "<br/>O preco do produto e R$ " .number_format($preco, 2);
    $preco += $preco*10/100; 
    ///se você quiser dar um desconto e so altera "+" por "-" que vai dar desconto.
    echo "<br/>O preço com 10% de aumento sera R$ " .number_format($preco, 2);
?>

</body>
</html>