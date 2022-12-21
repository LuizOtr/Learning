


//            esse símbolo aqui, que é o menor, é o lacinho. é como se fosse uma setinha pra esquerda e um desenho de uma seta.
// <Variável> <- <expressão>
//          Lê-se"recebe"

// Ele é então dado pelo comando de atribuição e a sintaxe.
// Ou seja, o jeito de se escrever esse comando é muito simples
// você vai colocar uma variável do lado
// esquerdo, você vai colocar esse símbolo aqui, o que é um menor
// e um bracinho, e depois você vai colocar
// uma expressão do lado direito.

// essa expressão que você colocar aqui
// do lado direito ela vai ser processada e o
// resultado da expressão vai ir para dentro da
// variável que tiver aqui do lado esquerdo

//Exemplo:

//Algoritmo "Exemplo"

//Var

//   x, y : inteiro

//Inicio

//      x <- 15
//      y <- 3 * x //Ao invés de colocar o cinco direto aqui, eu vou reaproveitar já a variável x.
      
//      escreval(x)
//      escreval(y)


//Fimalgoritmo



///////////////////////////////////////////////////////////////////////////


// Vamos supor que você tem lá duas variáveis X do tipo inteiro e
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


// Imagina que você tem aqui a área de um trapézio.
// A base maior do trapézio vale oito, a base menor
// vale seis e a altura vale cinco.

// Fórmula que é a média das duas bases, ou seja, B1, mas B2,
// tudo isso dividido por dois.
// E depois eu vou multiplicar pela altura essa que a fórmula.

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



// O operador de divisão inteira é esse aqui
//  e a barra invertida esse daqui "\".


//Exemplo 5

Algoritmo "Exemplo 5"

Var
    a : real
    b : inteiro

Inicio

a <- 5.0
b <- a // ERRO                   SOLUÇÃO: b <- Int(a)

escreval(b)

Fimalgoritmo


// O que você não pode simplesmente atribui um conteúdo de uma variável
// que é real para uma variável que é inteira. Por quê?
// Porque você perderia a informação. No caso aqui do exemplo,
// que é 5,0, até que não tem muito problema.
// Mas imagina se fosse 5,3, você perderia essa informação aqui?
// Então, nesse caso, você vai ter que fazer aqui um macete para
// explicitamente falar para o interpretador que
// você não importa com uma possível perda de informação.


   // SOLUÇÃO: b <- Int(a)
// Nesse caso, você vai ter que usar uma função chamada INT.
// Você vai fazer que a variável B recebe somente a parte
// inteira da variável A. Se você fizer assim, o interpretador vai aceitar.
