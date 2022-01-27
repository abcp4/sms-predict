
# SMS Predict

Aplicação que utiliza aprendizado de máquina para predizer se um SMS deve ser bloqueado ou não.

### Pré-requisitos

Antes de começar, é necessário ter instalado [Git](https://git-scm.com), [Docker][docker] e [docker-compose][compose]. Caso opte por executar as aplicações separadamente, acesse a pasta [api](api) e [webapp](webapp) e siga as instruções dos READMEs de cada.

### 🎲 Rodando a aplicação

```bash
# clone este repositório
$ git clone https://github.com/abcp4/sms-predict.git

# acesse a pasta do projeto
$ cd sms-predict

# Gere o modelo utilizado
$ cd experimento
$ pip install -r requirements.txt
$ dvc pull data/raw/train_data.cs
$ dvc repro

# execute o docker-compose
$ docker-compose up --build

# A aplicação iniciará na porta:8501 - disponível em http://0.0.0.0:8501
```
A documentação da API estará disponível em http://0.0.0.0:8000/docs



[docker]: https://docs.docker.com/engine/install/
[streamlit]: https://streamlit.io/
[fastapi]: https://fastapi.tiangolo.com/
[compose]: https://docs.docker.com/compose/