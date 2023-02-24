
//Quatro variáveis a variável
//A. que vai ser do tipo inteiro,
//	variável B. do tipo número real variável
//	C, que é caracter para guardar um texto.
//	E. a variável d do tipo lógico que é para
//	guardar o valor verdadeiro ou falso.

// Exemplo:

// Programa "Teste_saida

// Var

// 	a : inteiro
// 	b : real
// 	c : caractere
// 	d : logioco

// Inicio

//	a <- 32
//	b <- 2.34567
//	c <- "Bom dia!"
//	d <- VERDADEIRO

// Fimalgoritimo

 Algoritmo "Teste_saida

 Var

 	a : inteiro
 	b : real
 	c : caractere
 	d : logico

 Inicio

	a <- 32
	b <- 2.34567
	c <- "Bom dia!"
	d <- VERDADEIRO
	
	escreval(a)
	escreval       // saltar uma linha
	escreval(b)
    escreval(b:10) // Ele imprimiu o valor com dez espaços.
    escreval(b:10:2)
    escreval(c)
    escreval(d)
    
Fimalgoritmo

// se quiser saltar uma linha,
// pode simplesmente colocar o escreva.

// (b:10)
// Esse é o resultado de você
// colocar dois pontos, dez
// aqui na frente.

// Se você colocasse dois pontos,
// um outro valor, ele iria usar aquele
// número de caracteres que você colocasse.

// (b:10:2)
// Repare o seguinte agora ele está usando os dez
// caracteres aqui para imprimir.
// Só que ele está colocando duas casas decimais no final
// E repare também que ele fez o arredondamento.


//         Escrevendo mais de uma expressão de uma só vez

// Olha só como você faz para escrever mais
// de uma expressão de uma só vez.
// Vamos supor aqui que você tem uma variável
// idade valendo 32, uma variável salário
// valendo 4.560,9 e uma variável nome valendo Maria Silva.





Algoritmo "Escrevendo mais de uma expressão de uma só vez"

Var
   idade : inteiro
   salario : real
   nome : caracter
Inicio

      idade: <- 28
      salario: <- 1560.9
      nome: <- "Luiz Cordeiro"

      escreval("O Funcionario", nome, "ganha", salario:8:2 "e tem", idade, "anos.")


Fimalgoritmo

// Eu posso colocar ao mesmo tempo frases
// entre aspas e também variáveis,
// e tudo isso vai ser mostrado na tela.
// tem que separar eles por virgula !!







