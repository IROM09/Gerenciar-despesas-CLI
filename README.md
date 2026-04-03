
 Gerenciador de Gastos CLI

Este é um projeto em Python desenvolvido para gerenciar gastos de forma simples diretamente pelo terminal (CLI).

O sistema permite registrar despesas com nome, categoria, descrição e valor, organizando automaticamente os dados em diferentes categorias para facilitar o controle financeiro.

 Funcionalidades

- Adicionar novos gastos  
- Organizar por categorias:
  - Comida  
  - Higiene  
  - Casa  
  - Lazer  
  - Imprevisto  
- Visualizar todos os gastos cadastrados  
- Interface interativa via terminal  

## Como o sistema funciona

O programa utiliza uma estrutura baseada em dicionários para armazenar os gastos em memória durante a execução.

Cada categoria possui seu próprio dicionário, onde:
- A chave representa o nome do gasto  
- O valor é uma tupla contendo descrição e valor  

Exemplo:

{
  "Arroz": ("mercado", 20.0)
}

A interação com o usuário é feita através de um menu em loop (while), permitindo múltiplas operações até que o usuário escolha sair do programa.

 Estrutura do Projeto

* interface.py: Interface CLI e interação com o usuário
* cat.py: Lógica e estrutura de armazenamento dos gastos

 Como executar

1. Certifique-se de ter o Python instalado (3.x)
2. Execute o arquivo principal:

python interface.py

 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* Prática de lógica de programação
* Uso de estruturas de dados (dicionários)
* Organização de código em múltiplos arquivos
* Interação via terminal (CLI)

 Observação

Os dados são armazenados apenas em memória durante a execução do programa. Ao fechar o sistema, as informações são perdidas.

 Possíveis melhorias

* Persistência de dados com JSON - Feito
* Interface gráfica ou web
* Sistema de login de usuário
* Relatórios e totais de gastos
