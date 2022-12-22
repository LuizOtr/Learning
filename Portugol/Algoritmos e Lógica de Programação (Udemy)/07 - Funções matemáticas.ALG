
//Algumas funções matemáticas
//Exemplo Significado


// A <- RaizQ(x)  = Variável A recebe a raiz quadrada de x
// A <- Exp(x, y) = Variável A recebe o resultado de x elevado a y
// A <- Pi Variável A recebe o valor de Pi
// A <- Abs(x) Variável A recebe o valor absoluto de x

//Exemplo


Algoritmo "Funções matemáticas"

Var

   x, y, z, a, b, c, d : real

Inicio

   x <- 2.0
   y <- 3.0
   z <- -7.0
   a <- Exp(x, y)
   b <- RaizQ(y)
   c <- Pi
   d <- Abs(z)

   escreval(a)
   escreval(b)
   escreval(c)
   escreval(d)

Fimalgoritmo