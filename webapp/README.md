# Webapp

Essa aplicação foi construída com o propósito de realizar uma investigação sobre quais variáveis contribuem para a predição do modelo. Utilizamos o algoritmo de explicabilidade SHAP.

## :hammer_and_wrench: Como executar o projeto

Esta aplicação precisa que a API esteja em execução para funcionar.

### Pré-requisitos

Antes de começar é necessário possuir o Python 3 instalado em seu sistema operacional, de preferência a versão 3.9, além disso é necessário o [Git](https://git-scm.com/) para realizar os passos abaixo. 

### :spider_web: Rodando a aplicação

#### :snake: Opção 1: Python

```bash
# clone este repositório
$ git clone https://github.com/abcp4/sms-predict.git

# acesse a pasta do projeto
$ cd sms-predict

# em seguida acessa a pasta webapp
$ cd webapp

# instale as dependências necessárias
$ pip install -r requirements.txt

# execute a aplicação
$ streamlit run main.py
```

O servidor iniciará na porta:8501 e a aplicação ficará disponível http://localhost:8501/.