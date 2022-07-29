# Flask Contact

Desenvolvimento de um simples CRUD considerando a Entidade conforme Figura-1.
<p>

![image](https://user-images.githubusercontent.com/16855746/181521873-a9b4afe0-1d15-438f-ba3e-de441c3b5c44.png)
<br/>
Figura-1


## Preparando a aplicação

### 1. Verifique se o Python já está instalado

```
$ python3 --version
```

ou

```
$ python --version
```

### 2. Se Python 2.7 ou posterior não estiver instalado, instale Python com o gerenciador de pacote de distribuição.

```
$ sudo apt-get install python3
```

### 3. Para verificar se o Python foi instalado corretamente, abra um prompt de comando ou shell e execute o comando a seguir.

```
$ python3 --version
```

### 4. Faça o clone do projeto para seu workspace local (antes verifique se você tem instalado o Git)

```
$ git clone https://github.com/luisrfpam/flaskcontact.git
```

#### 4.1 Instalando Git no Linux

```
$ sudo apt install git
```

#### 4.2 Verificando se a instalação do Git foi feita corretamente

```
$ git --version
```

### 5. Instalando Ambiente Virtual

Use o apt para instalar o virtualenv no Linux

```
$ sudo apt install python-virtualenv
```

### 6. Criando um Ambiente Virtual

Acesse o diretório do projeto

```
$ cd <folder project name>
```

Criando o ambiente virtual no Python3:

![image](https://user-images.githubusercontent.com/16855746/181496991-da9e49e8-4c76-4338-aeb6-bf79bb2b5696.png)

O virtualenv é realmente simples. Ele basicamente cria uma cópia de todos os diretórios necessários para que um programa Python seja executado, isto inclui:

- As bibliotecas comuns do Python (standard library);
- O gerenciador de pacotes pip;
- O próprio binário do Python (Python 2.x/3.x);
- As dependências que estiverem no diretório site-packages;
- Seu código fonte descrevendo sua aplicação.
- Assim, ao instalar uma nova dependência dentro do ambiente criado pelo virtualenv, ele será colocado no diretório site-packages relativo à esse ambiente, e não mais globalmente.

```
$ python3 -m venv <name of environment>
	
$ python3 -m venv env
```

### 7. Ativando o ambiente virtual

Você precisar ativar o ambiente virtual e para isso execute no seu terminal

```
$ . <name of environment>/bin/activate
	
$ . env/bin/activate	
```
	
ou
	
```
$ source env/bin/activate	
```

### 8. Instalando as dependências do Projeto

#### 8.1 Flask-RESTful

```
$ pip install Flask-RESTful
```

Flask é instalado automaticamente com todas as dependências.

#### 8.2 Instalando DotEnv
	
O dotenv é usado para ler o par de chave e valor do arquivo .env e adicioná-lo à variável de ambiente. Podemos usá-lo para gerenciar as configurações do aplicativo durante as fases de desenvolvimento e produção

```
$ pip install python-dotenv 
```
	
----------------------------------------------------------------------------------------------------------
## API Flask Contact
	
Após configurar a API vamos colocá-la em operação!

### 9. Iniciando aplicação Flask Contact
	
Acesse o diretório do projeto 

```
$ cd <folder project name>
```

Vamos configurar uma variável de ambiente
	
```
$ export FLASK_CONTACT=app.py
```

Após configurado vamos rodar o Flask para iniciar o servidor ```http://127.0.0.1:5000/```

```
$ flask run
```
	
Se tudo ocorrer bem :) Irá aparecer para você a mensagem no terminal Running on ```http://127.0.0.1:5000/```
<br />
Agora você pode consumir a API!!!
	
### 10. Para fazer as requisições vamos utilizar o curl no terminal do Linux
#### 10.1 Instalando o CURL no Linux

```
$ sudo apt install curl
```

### 11. Utilizando a API

#### HTTP Verbs

GET 
	
Listar todos os contatos: GET /contacts	
```
$ curl -o saida.json http://127.0.0.1:5000/contacts/
```
Retorna: 200 OK
```JSON
{
    "data": [
        {
            "cpf": "88889577320",
            "email": "luis@gmail.com",
            "endereco": "Rua Vicente Menezes, n.100, Alto Rio",
            "nome": "Luis Roberto Marinho",
            "telefone": "92984030269"
        },
        {
            "cpf": "98684577420",
            "email": "carlos@gmail.com",
            "endereco": "Rua Castro Alves, n.45, São Jose",
            "nome": "Carlos Eduardo Silva",
            "telefone": "19994090268"
        },
        {
            "cpf": "46574977320",
            "email": "pedro@gmail.com",
            "endereco": "Rua Rio Negro, n.14, Lirio do Vale",
            "nome": "Pedro Henrique Silvestre",
            "telefone": "17994020368"
        },
        {
            "cpf": "90434277310",
            "email": "paulo@gmail.com",
            "endereco": "Rua Eduardo Ribeiro, n.104, Centro",
            "nome": "Luis Paulo Freire",
            "telefone": "51984040360"
        }
    ],
    "message": "Recurso(s) Contacts recuperado.",
    "resource": "Contacts",
    "status": 200
}
```

<p>
	
Listar um contato passando como paramêtro o CPF (se existir): GET /contacts/88889577320
```
$ curl -o saida.json http://127.0.0.1:5000/contacts/88889577320
```

Retorna: 200 OK
```JSON
{
    "data": {
        "cpf": "88889577320",
        "email": "luis@gmail.com",
        "endereco": "Rua Vicente Menezes, n.100, Alto Rio",
        "nome": "Luis Roberto Marinho",
        "telefone": "92984030269"
    },
    "message": "Recurso(s) Contacts recuperado.",
    "resource": "Contact",
    "status": 200
}
```

<p>
	
Listar um contato passando como paramêtro o CPF (se não existir): GET /contacts/88889577328
```
$ curl -o saida.json http://127.0.0.1:5000/contacts/88889577328
```

Retorna: 200 OK
```JSON
{
    "message": "Recurso Sem dados.",
    "resource": "Contact",
    "status": 200
}
```

POST

Salvar um contato: POST /contacts
```
$ curl -X POST -H 'Content-Type: application/json' -d { "cpf": "12365670900", "nome": "Felipe Bastos", "endereco" : "Rua Central Campinas, n.01, São Paulo", 
"telefone" : "19997457967", "email" : "felipe@gmail.com" } http://127.0.0.1:5000/contacts
```

data:
```JSON
{
  "cpf": "12365670900",
  "nome": "Felipe Bastos",
  "endereco" : "Rua Central Campinas, n.01, São Paulo",
  "telefone" : "19997457967",
  "email" : "felipe@gmail.com"	
}
```

Retorna: 201 CREATED
```JSON
{
    "data": {
        "cpf": "12365670900",
        "email": "felipe@gmail.com",
        "endereco": "Rua Central Campinas, n.01, São Paulo",
        "nome": "Felipe Bastos",
        "telefone": "19997457967"
    },
    "message": "Recurso Contacts criado.",
    "resource": "Contacts",
    "status": 201
}
```

PUT

Atualizar um contato existente passando como parâmetro o CPF: PUT /contacts/12365670900
```
$ curl -X PUT -H 'Content-Type: application/json' -d {"nome": "Felipe Bastos Castro", "endereco" : "Rua Joaquim Marcelino, n.126, São Paulo",
    "telefone" : "19997457967", "email" : "felipe@gmail.com"} http://127.0.0.1:5000/contacts/12365670900
```

data:
```JSON
{
  "nome": "Felipe Bastos Castro",
  "endereco" : "Rua Joaquim Marcelino, n.126, São Paulo",
  "telefone" : "19997457967",
  "email" : "felipe@gmail.com"
}
```

Retorna: 200 OK
```JSON
{
    "data": {
        "cpf": "12365670900",
        "email": "felipe@gmail.com",
        "endereco": "Rua Joaquim Marcelino, n.126, São Paulo",
        "nome": "Felipe Bastos Castro",
        "telefone": "19997457967"
    },
    "message": "Recurso Contacts atualizado.",
    "resource": "Contact",
    "status": 200
}
```

<p>

Atualizar um contato não existente passando como parâmetro o CPF: PUT /contacts/12365670901
```
$ curl -X PUT -H 'Content-Type: application/json' -d {"nome": "Felipe Bastos Castro", "endereco" : "Rua Joaquim Marcelino, n.126, São Paulo",
    "telefone" : "19997457967", "email" : "felipe@gmail.com"} http://127.0.0.1:5000/contacts/12365670901
```

data:
```JSON
{
  "nome": "Felipe Bastos Castro",
  "endereco" : "Rua Joaquim Marcelino, n.126, São Paulo",
  "telefone" : "19997457967",
  "email" : "felipe@gmail.com"
}
```

Retorna: 404 NOT FOUND
```JSON
{
    "message": "Este(a) contato não existe.",
    "resource": "Contact"
}
```

DELETE

Deletar um contato existente passando como paramêtro o CPF: DELETE /contacts/88889577320
```
$ curl -X DELETE http://127.0.0.1:5000/contacts/88889577320
```

Retorna: 204 No Content
	
<p>
	
Deletar um contato não passando como paramêtro o CPF: DELETE /contacts/88889577321
```
$ curl -X DELETE http://127.0.0.1:5000/contacts/88889577321
```

Retorna: 404 NOT FOUND
```JSON
{
    "message": "Este(a) contato não existe.",
    "resource": "Contact"
}
```

----------------------------------------------------------------------------------------------------------
## API Flask com TDD
Nesta seção vamos trabalhar com TDD (Testes automatizados)
	
### 12. Instalando o PyTest

```
$ sudo apt-get install python-pytest
```

O Pytest é um framework ou uma ferramenta para escrever testes no desenvolvimento de software e bibliotecas em Python.
Vamos precisar instalar o DotEnv também.

#### Lembre-se que antes de instalar qualquer lib você deve está com o Ambiente Virtual ativado


