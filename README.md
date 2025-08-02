# Sistema Bancário em Python
Este projeto é uma aplicação simples em Python que simula um sistema bancário. Ele permite realizar operações como depósito, saque e exibição de extrato, com limites e validações.

## Funcionalidades
#### Operação de Depósito:

- Permite depositar valores positivos na conta.
- Armazena cada operação no extrato.

#### Operação de Saque:

- Permite realizar até 3 saques diários.
- Cada saque tem um limite máximo de R$ 500,00.
- Verifica se há saldo suficiente antes de realizar a operação.
- Armazena cada saque no extrato.

#### Operação de Extrato:

- Exibe todas as movimentações financeiras (depósitos e saques).
- Mostra o saldo atual da conta.
- Indica a ausência de movimentações, caso não haja nenhuma.

#### Menu Interativo:

Interface simples para facilitar a navegação entre as operações:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


## Como Executar o Projeto

#### Pré-requisitos
- Python 3.8 ou superior instalado no seu sistema.
- Editor de texto ou IDE para rodar o programa (como VSCode, PyCharm ou IDLE).
Passos para execução
- Clone o repositório ou copie o código para um arquivo chamado sistema_bancario.py.
- No terminal, navegue até o diretório onde o arquivo está salvo.
- Execute o programa com o comando:
```
python sistema_bancario.py
```

## Exemplo de Uso

#### Menu Principal
- Ao executar o programa, você verá o menu interativo:
```
    =========== MENU ===========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> 
```

#### Depósito
- Escolha a opção 1.
- Insira o valor do depósito (exemplo: 1500.00).
- Resultado:
```
Depósito de R$ 1500.00 realizado com sucesso!
```
#### Saque
- Escolha a opção 2.
- Insira o valor do saque (exemplo: 500.00).
- O sistema validará:
  - Se há saldo suficiente.
  - Se o valor não excede o limite por saque.
  - Se ainda há saques disponíveis para o dia.
- Resultado:
```
Saque de R$ 500.00 realizado com sucesso!
```

#### Extrato
- Escolha a opção 3.
- Exemplo de extrato:
```
========== EXTRATO ==========
Depósito:       + R$ 1500.00
Saque:          - R$ 500.00

Saldo: R$ 1000.00
=============================
```

## Possíveis Melhorias
- Implementar suporte para múltiplos usuários com autenticação.
- Controlar os saques diários com base na data.

## Tecnologias Utilizadas
- Linguagem: Python 3
- Estruturas de dados: Listas e variáveis primitivas

## Autor

- [**Juliana Guimarães de Farias**](https://github.com/jugfarias)  
  - Desenvolvedora do sistema bancário simples, com uso do template do Santander Bootcamp Python 2025, com foco em aprendizado e boas práticas de programação em Python.