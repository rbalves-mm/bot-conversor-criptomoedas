# Robô para Telegram: envia rendimentos em criptomoedas

Este projeto consiste em um robô desenvolvido em Python que converte unidades de criptomoedas em Real Brasileiro.

## Recursos utilizados
* [Telebot](https://telepot.readthedocs.io/en/latest/#)
* [ADVFN API](https://br.advfn.com/)

## Pré-requisitos
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/)

## Instalando e executando
1. Clonar o projeto: **git clone https://github.com/rbalves-mm/bot-conversor-criptomoedas**
2. Navegue até a pasta bot-conversor: **cd bot-conversor-criptomoedas**
2. Criar o arquivo no formato JSON com a sua lista de criptomoedas, conforme o modelo apresentado no arquivo 'moedas-exemplo.json'
3. Criar bot no Telegram usando o [BotFather](https://core.telegram.org/bots)
4. Criar o arquivo 'token.txt' e setar o token do bot criado
4. Executar o comando abaixo para buildar o projeto
```
docker build -t bot-conversor-criptomoedas .
```
5. Executar o comando abaixo para executar o projeto
```
docker run -it --rm --name bot-conversor-criptomoedas bot-conversor-criptomoedas
```

## Autores

* **Rafael Alves** - *Initial work* - [LinkedIn](https://www.linkedin.com/in/rbalves192/)
