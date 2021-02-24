import requests
import telepot
import json
from datetime import datetime
import os

urlBase = 'https://br.advfn.com/common/cryptocurrency/converter/api/getConversion'

def obterToken():
    caminho = "token.txt"

    validarArquivo(caminho)

    arquivo = open("token.txt")
    token = arquivo.read()
    arquivo.close()

    return token

def validarArquivo(caminho):
    if not os.path.exists(caminho):
        raise Exception("O arquivo '" + caminho + "' não foi encontrado")

    if os.stat(caminho).st_size == 0:
        raise Exception("O arquivo '" + caminho + " ' está vazio")

def iniciarBot():
    token = obterToken()
    bot = telepot.Bot(token)
    return bot

def obterMoedas():
    caminho = 'moedas.json'

    validarArquivo(caminho)

    arquivo = open(caminho)
    criptomoedas = json.load(arquivo)
    arquivo.close()

    return criptomoedas

def obterMensagemRendimentos():
    mensagem = ''
    titulo = 'MEUS RENDIMENTOS'
    divisor = '-------------------------------------------------------'
    mensagem = mensagem + titulo + '\n' + divisor

    rendimentoTotal = 0

    for moeda in obterMoedas():
        url = f'{urlBase}?from={moeda["codigo"]}&to=BRL&amount={moeda["unidades"]}'
        response = requests.get(url)

        valorConvertido = response.json()['conversion']
        valorFormatado = response.json()['conversion_unformatted']

        rendimentoTotal = rendimentoTotal + valorFormatado

        mensagem = mensagem + '\n' + moeda['descricao'] + ': ' + str(moeda['unidades'])
        mensagem = mensagem + '\n' + 'Real: ' + str(valorConvertido)
        mensagem = mensagem + '\n' + divisor

    mensagem = mensagem + '\n' + 'TOTAL: ' + str(rendimentoTotal)

    return mensagem

def obterChatId():
    bot = iniciarBot()
    primeiro, *resto = bot.getUpdates()
    chat_id = primeiro['message']['chat']['id']
    return chat_id

def log(mensagem):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('[' + dt_string + '] ' + mensagem)

def enviarMensagem():
    bot = iniciarBot()
    chat_id = obterChatId()
    mensagem = obterMensagemRendimentos()
    bot.sendMessage(chat_id, mensagem)
    log('MENSAGEM ENVIADA')

if __name__ == "__main__":
    try:
        enviarMensagem()
    except Exception as exception:
        print(exception)
