### Pré-requisitos

Antes de começar é necessário possuir o Python 3 instalado em seu sistema operacional, de preferência a versão 3.9, além disso é necessário o [Git](https://git-scm.com/) para realizar os passos abaixo. 

> É possível também executar a aplicação através do docker.

### :spider_web: Rodando a aplicação

#### :snake: Opção 1: Python

```bash
# clone este repositório
$ git clone https://github.com/abcp4/sms-predict.git

# acesse a pasta do projeto
$ cd sms-predict

# em seguida acessa a pasta da api
$ cd api

# instale as dependências necessárias
$ pip install -r requirements.txt

# execute a aplicação
$ uvicorn main:app --reload
```

#### :whale2: Opção 2: Docker

```
# clone este repositório
$ git clone https://github.com/abcp4/sms-predict.git

# acesse a pasta do projeto
$ cd sms-predict

# em seguida acessa a pasta da api
$ cd api

# construir a imagem docker
$ docker build -t api-sms:latest .

# executar imagem
$ docker run -d -v $PWD/../experimento/data/models:/api/models \
    --name=api-predict \
    -p 8000:8000 api-sms:latest
```

O servidor iniciará na porta:8000 e a documentação estará acessível em http://localhost:8000/docs.