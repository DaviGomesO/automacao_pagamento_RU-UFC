# Automacao_pagamento_RU-UFC
Essa automação serve para facilitar o fluxo da inserção de créditos do cartão do Restaurante Universitário da Universidade Federal do Ceará.

#### Passos:
1. Após clonar o projeto, crie o ambiente virtual python, e ative-o para instalar as dependências/bibliotecas do projeto.
  - Criar ambiente virtual: python -m venv nome_do_ambiente;
  - Ativar: nome_do_ambiente\Scripts\activate
2. Instalar as seguintes bibliotecas no ambiente virtual:
  - pip install selenium
  - pip install python-dotenv
3. Inserir um arquivo '.env' junto ao executável para o carregamento dos dados, onde os mesmos obrigatoriamente tem de está do seguinte formato:
<pre>
<b>NUMERO_CARTAO='xxxxxxxx'
MATRICULA='xxxxxx'
QUANTIDADE_CREDITOS=xx</b>
</pre>

### Translate
# Automacao_pagamento_RU-UFC
This automation serves to facilitate the flow of inserting credits into the University Restaurant card at the Federal University of Ceará.

#### Steps:
1. After cloning the project, create the python virtual environment, and activate it to install the project's dependencies/libraries.
  - Create virtual environment: python -m venv environment_name;
  - Activate: environment_name\Scripts\activate
2. Install the following libraries in the virtual environment:
  - pip install selenium
  - pip install python-dotenv
3. Insert a '.env' file next to the following to load the data, which must have the following format:
<pre>
<b>NUMERO_CARTAO='xxxxxxx'
MATRICULA='xxxxxx'
QUANTIDADE_CREDITOS=xx</b>
```
</pre>
