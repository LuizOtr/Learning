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
    $a = 3;
    $b = $a; #se colocar uma varialvel "&" na frente do $a, automaticamente vou estar criando uma referencia de varival "B" a variavel "A"
    $b += 5;
    echo "A variavel A vale $a";
    echo "<br/> A variavel B vale $b";
?>
    
</body>
</html>