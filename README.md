# ariel

# Documentação do Programa de Conversão e Cálculo de Números

O programa de conversão e cálculo de números é um código em Python que permite converter números decimais para binários e octais, converter números binários e octais para decimais, e realizar operações aritméticas (soma e subtração) com números binários.

## Uso do Programa

Ao executar o programa, será apresentado um menu de opções com as seguintes escolhas:

1. Converter número decimal para binário e octal
2. Converter números binários e octais para decimal
3. Calculadora aritmética de números binários (soma e subtração)
4. Sair

## Opção 1: Converter número decimal para binário e octal

Nessa opção, o usuário pode digitar um número decimal. O programa irá converter esse número para sua representação binária e octal utilizando as funções `bin()` e `oct()` respectivamente. Em seguida, os resultados das conversões serão exibidos na tela.

## Opção 2: Converter números binários e octais para decimal

Nessa opção, o usuário pode escolher entre converter um número octal ou um número binário. O programa solicitará o número na respectiva base escolhida. Em seguida, utilizará a função `int()` com a base correta (8 para octal e 2 para binário) para converter o número para sua representação decimal. O resultado da conversão será exibido na tela.

## Opção 3: Calculadora aritmética de números binários (soma e subtração)

Nessa opção, o programa oferece uma calculadora aritmética para números binários. O usuário deverá inserir dois números binários e escolher a operação desejada: soma (+) ou subtração (-). O programa utilizará as funções `binario_adic()` e `binario_sub()` para realizar as operações de soma e subtração binárias respectivamente. O resultado da operação será exibido na tela.

## Encerramento

Ao selecionar a opção 4 (Sair), o programa será encerrado.

## Observações

- O programa valida as entradas do usuário e trata possíveis erros, como números binários inválidos.
- O código está estruturado com loops `while` para permitir que o usuário execute várias operações consecutivas.
- A documentação mencionou brevemente as funções `binario_adic()` e `binario_sub()`, mas seus detalhes de implementação não foram fornecidos no código apresentado.

Esperamos que esta documentação ajude a compreender e utilizar o programa de conversão e cálculo de números.
