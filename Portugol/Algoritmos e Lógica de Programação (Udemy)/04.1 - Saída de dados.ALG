
//Quatro vari�veis a vari�vel
//A. que vai ser do tipo inteiro,
//	vari�vel B. do tipo n�mero real vari�vel
//	C, que � caracter para guardar um texto.
//	E. a vari�vel d do tipo l�gico que � para
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
    escreval(b:10) // Ele imprimiu o valor com dez espa�os.
    escreval(b:10:2)
    escreval(c)
    escreval(d)
    
Fimalgoritmo

// se quiser saltar uma linha,
// pode simplesmente colocar o escreva.

// (b:10)
// Esse � o resultado de voc�
// colocar dois pontos, dez
// aqui na frente.

// Se voc� colocasse dois pontos,
// um outro valor, ele iria usar aquele
// n�mero de caracteres que voc� colocasse.

// (b:10:2)
// Repare o seguinte agora ele est� usando os dez
// caracteres aqui para imprimir.
// S� que ele est� colocando duas casas decimais no final
// E repare tamb�m que ele fez o arredondamento.


//         Escrevendo mais de uma express�o de uma s� vez

// Olha s� como voc� faz para escrever mais
// de uma express�o de uma s� vez.
// Vamos supor aqui que voc� tem uma vari�vel
// idade valendo 32, uma vari�vel sal�rio
// valendo 4.560,9 e uma vari�vel nome valendo Maria Silva.





Algoritmo "Escrevendo mais de uma express�o de uma s� vez"

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
// entre aspas e tamb�m vari�veis,
// e tudo isso vai ser mostrado na tela.
// tem que separar eles por virgula !!







