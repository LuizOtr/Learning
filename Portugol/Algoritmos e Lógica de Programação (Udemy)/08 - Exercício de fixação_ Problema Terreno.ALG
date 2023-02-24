
//Problema "terreno"

// Fazer um programa para ler as medidas da largura e
// comprimento de um terrenoretangular com uma casa decimal,
// bem como o valor do metro quadrado do terreno com duas casas decimais.
// Em seguida, o programa deve mostrar o valor da área do terreno,
// bem como o valor do preço do terreno, ambos com duas casas decimais




Algoritmo "Problema Terreno"


Var

   l, c, m : real
   a, v :real

Inicio



      escreval("Qual a largura do terreno: ")
      leia(l)
      escreval("Qual e o comprimento: ")
      leia(c)
      escreval("Qual o valor do metro quadrado: ")
      leia(m)
      
      a <- l*c
      v <- a*m
      
      escreval("Area do terreno: ",a:5:2)
      escreval("Preço do terreno: ",v:7:2)

Fimalgoritmo