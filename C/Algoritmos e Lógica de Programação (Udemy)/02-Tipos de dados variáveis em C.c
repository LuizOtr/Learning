// bibliotecas 

#include <stdio.h>
#include <string.h> //função para trabalhar com strings ou seja trabalhar com texto 

// assinatura do programa

int main () {

    // Variaveis

    int idade;   // segundo metodo - int idade = 20;
    double salario, altura;
    char genero;
    char nome[50]; // *segundo metodo - char nome[50]; ="Maria Silva";

    // atribuições

    idade = 20;
    salario = 5800.5;
    altura = 1.63;
    genero = 'F';
    strcpy (nome, "Maria Silva");  // *segundo metodo
    
    /* strcpy = função para trabalhar com texto */
    


    // Impressões das variaveis

    printf("IDADE = %d\n", idade);   // No caso de número interito coloca "%d" 
    printf("SALARIO = %.2lf\n", salario);
    printf("ALTURA = %.2lf\n", altura);
    printf("GENERO = %c\n", genero);
    printf("NOME = %s\n", nome);

    return 0;
}

/*
Número inteiro = int
Número de ponto flutuante = double
Um único caractere = char
Texto = char [ ]
valor lógico = int
*/

/*

int main (){

    int x;

    printf("%d", x);

    return 0;
}

vai retornar um lixo de memória que estiver disponível ou seja valor aleatório

*/