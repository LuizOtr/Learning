<?php 
    
    if(isset($_POST['email']) && !empty($_POST['email']))

    $name = addslashes($_POST['name']);
    $email = addslashes($_POST['email']);
    $mensagem = addslashes($_POST['mensagem']);

    $to = "contato@gmail.com";
    $subject = "Contato - ping BR";
    $body = "Nome: ".$name. "\r\n".
            "Email: ".$email. "\r\n".
            "Mensagem: ".$mensagem;

    $header = "Fron:contato@gmail.com"."\r\n"
        ."Reply-To".$email."\e\n"
        ."X=Mailer:PHP/".phpversion();
    
    if(mail($to,$subject,$body,$header)){

        echo("Email enviado com sucesso!");
    
    }else{
        echo("O Email não pode ser enviado");
        }
?>