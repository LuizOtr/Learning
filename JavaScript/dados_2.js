let preco = 19.90;
let desconto = 0.4;


// Então quando você vê um código desse você não tem a menor ideia do que se trata

console.log(19.90 * 0.6);

//E quando você vê um código desse fica muito mais fácil saber que você está calculando o preço com desconto

// "(preco * (1 - desconto));" que ele vai fazer ele vai pagar o preço multiplicado por um e vai subtrair apenas o valor zero ponto 4

console.log(preco * (1 - desconto));

// Ele vai concatenar colocar um texto do lado do outro

let nome = "Caderno"; // String (Texto) -> sequencia de símbolos
let categoria = "Papelaria";
console.log("Produto: " + nome
    + ", Categoria: " + categoria
    + ", Preço: " + preco
    + ", Desconto: " + desconto); // estou mesclando um pouco de texto literal mas o valor de uma variável.

