
//              Problema "retangulo"
// Fazer um programa para ler as medidas da base e altura de um ret�ngulo.
// Em seguida, mostrar o valor da �rea, per�metro e diagonal
// deste ret�ngulo, com quatro casas decimais.

Algoritmo "Problema Retangulo"

Var

   at, ar : real
   a, v, d :real

Inicio

      escreval("Qual a base do retangulo: ")
      leia(at)
      escreval("Qual e altura: ")
      leia(ar)

      a <- at*ar
      v <- 2 * ( at + ar )
      d <- RaizQ(Exp(at, 2) + Exp(ar, 2))
      //d) isso aqui eu estou falando eu quero a exponencia��o de base elevado
      // a segunda pot�ncia que � base ao quadrado.

      escreval("Area: ",a:8:4)
      escreval("Perimetro: ",v:8:4)
      escreval("Diagonal: ",d:8:4)
      
Fimalgoritmo