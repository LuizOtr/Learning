


//            esse s�mbolo aqui, que � o menor, � o lacinho. � como se fosse uma setinha pra esquerda e um desenho de uma seta.
// <Vari�vel> <- <express�o>
//          L�-se"recebe"

// Ele � ent�o dado pelo comando de atribui��o e a sintaxe.
// Ou seja, o jeito de se escrever esse comando � muito simples
// voc� vai colocar uma vari�vel do lado
// esquerdo, voc� vai colocar esse s�mbolo aqui, o que � um menor
// e um bracinho, e depois voc� vai colocar
// uma express�o do lado direito.

// essa express�o que voc� colocar aqui
// do lado direito ela vai ser processada e o
// resultado da express�o vai ir para dentro da
// vari�vel que tiver aqui do lado esquerdo

//Exemplo:

//Algoritmo "Exemplo"

//Var

//   x, y : inteiro

//Inicio

//      x <- 15
//      y <- 3 * x //Ao inv�s de colocar o cinco direto aqui, eu vou reaproveitar j� a vari�vel x.
      
//      escreval(x)
//      escreval(y)


//Fimalgoritmo



///////////////////////////////////////////////////////////////////////////


// Vamos supor que voc� tem l� duas vari�veis X do tipo inteiro e
// Y do tipo real.


//Exemplo: 2

//Algoritmo "Exemplo 2"

//Var

//   x : inteiro
//   y : real

//Inicio

//      x <- 5
//      y <- 2 * x

//      escreval(x)
//      escreval(y)

//Fimalgoritmo


// Imagina que voc� tem aqui a �rea de um trap�zio.
// A base maior do trap�zio vale oito, a base menor
// vale seis e a altura vale cinco.

// F�rmula que � a m�dia das duas bases, ou seja, B1, mas B2,
// tudo isso dividido por dois.
// E depois eu vou multiplicar pela altura essa que a f�rmula.

//Algoritmo "Exemplo 3"

//Var

//   b1, b2, h, area : real

//Inicio

//      b1 <- 6.0
//     b2 <- 8.0
//      h <- 5.0
      
//      area <- (b1 + b2) / 2.0 * h;
      
//      escreval(area)

//Fimalgoritmo



//Exemplo 4:

//Algoritmo "Exemplo 4"

//Var

//   a, b, resultado : inteiro

//Inicio

//    a <- 5
//    b <- 2
//    resultado <- a \ b - ERRO!

//    escreval(resultado)

//Fimalgoritmo



// O operador de divis�o inteira � esse aqui
//  e a barra invertida esse daqui "\".


//Exemplo 5

Algoritmo "Exemplo 5"

Var
    a : real
    b : inteiro

Inicio

a <- 5.0
b <- a // ERRO                   SOLU��O: b <- Int(a)

escreval(b)

Fimalgoritmo


// O que voc� n�o pode simplesmente atribui um conte�do de uma vari�vel
// que � real para uma vari�vel que � inteira. Por qu�?
// Porque voc� perderia a informa��o. No caso aqui do exemplo,
// que � 5,0, at� que n�o tem muito problema.
// Mas imagina se fosse 5,3, voc� perderia essa informa��o aqui?
// Ent�o, nesse caso, voc� vai ter que fazer aqui um macete para
// explicitamente falar para o interpretador que
// voc� n�o importa com uma poss�vel perda de informa��o.


   // SOLU��O: b <- Int(a)
// Nesse caso, voc� vai ter que usar uma fun��o chamada INT.
// Voc� vai fazer que a vari�vel B recebe somente a parte
// inteira da vari�vel A. Se voc� fizer assim, o interpretador vai aceitar.
