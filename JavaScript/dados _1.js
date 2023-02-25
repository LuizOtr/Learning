
/* var = É usada para armazenar e manipular valores que podem ser alterados durante a execução do programa. */

var nome = "Caneta azul";
var quantidade  = 10;
var preco = 6.4;
var imposto = 1.5;
//outro metodo de criar variavel e usar a palavra 'let' e a forma moderna no momento
let precoFinal = preco + imposto; 

console.log(nome);
console.log(quantidade);      // Valor literal
console.log(preco);
console.log(imposto);
console.log(precoFinal);

nome = "Caneta BIC";
console.log(nome);