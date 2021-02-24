# Robô para Telegram: envia rendimentos em criptomoedas

Este projeto consiste em um robô desenvolvido em Python que converte unidades de criptomoedas em Real Brasileiro e envia os dados para o Telegram.

## Recursos utilizados

- [Telebot](https://telepot.readthedocs.io/en/latest/#)
- [ADVFN API](https://br.advfn.com/)

## Pré-requisitos

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

## Instalando e executando

1. Clonar o projeto: **git clone https://github.com/rbalves-mm/bot-conversor-criptomoedas**
2. Navegue até a pasta bot-conversor: **cd bot-conversor-criptomoedas**
3. Criar o arquivo no formato JSON com a sua lista de criptomoedas, conforme o modelo apresentado no arquivo 'moedas-exemplo.json'
4. Criar bot no Telegram usando o [BotFather](https://core.telegram.org/bots)
5. Criar o arquivo 'token.txt' e setar o token do bot criado
6. Executar o comando abaixo para buildar o projeto

```
docker build -t bot-conversor-criptomoedas .
```

5. Executar o comando abaixo para executar o projeto

```
docker run -it --rm --name bot-conversor-criptomoedas bot-conversor-criptomoedas
```

## Informações adicionais

Há diversas maneiras de agendar a execução deste container com o bot, a fim de que a mensagem com os rendimentos seja enviada em intervalos de tempo. As opções listadas abaixo possuem uma série de tutoriais na web:

1. No Linux, é possível agendar tarefas através da ferramenta Crontab.
2. No Windows, é possível usar o Agendador de tarefas. Caso seja necessário, criar um bat para ser executado.

## Autores

- **Rafael Alves** - _Initial work_ - [LinkedIn](https://www.linkedin.com/in/rbalves192/)
