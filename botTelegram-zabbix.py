#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
##########################################################################
# BotTelegram Zabbix
# Filename: botTelegram-zabbix.py
# Revision: 1.0
# Revision_data: 30/05/2016
# Date: 30/05/2016
# Author: Diego Maia - diegosmaia@yahoo.com.br Telegram - @diegosmaia
# Aproveitei algumas ideias do https://github.com/python-telegram-bot/python-telegram-bot
##########################################################################

from telegram.ext import Updater, CommandHandler
import logging
import sys
import subprocess
import urllib

##########################################
# Para testes 
# python botTelegram-zabbix.py
#
# Para deixar rodando em bg 
# python botTelegram-zabbix.py&
#
##########################################

##########################################
# Vai ter que instalar o pyhton e o pip
# pip install telegram logging subprocess urllib --upgrade
# apt-get install python-urllib3
##########################################

##########################################
# Abir o Zabbix ir em monitoramento - > mapas
# No firefox vc clica com o direito encima do mapa e vai em ver imagem
# Copia a url e cola abaixo no mapa1 e assim por diante
# Neste exemplo você tem como coletar 5 mapas diferente
# Eu fiz um mapa com o status geral da rede e outros de cada filial
# Estou deixando o arquivo JPG de exemplo de como montei o meu mapa 
##########################################

varZabbixmapa1 = "http://192.168.10.24/zabbix/map.php?sysmapid=8&severity_min=5"
varZabbixmapa2 = "http://192.168.10.24/zabbix/map.php?sysmapid=2&severity_min=4"
varZabbixmapa3 = "http://192.168.10.24/zabbix/map.php?sysmapid=5&severity_min=4"
varZabbixmapa4 = "http://192.168.10.24/zabbix/map.php?sysmapid=6&severity_min=4"
varZabbixmapa5 = "http://192.168.10.24/zabbix/map.php?sysmapid=8&severity_min=5"


##########################################
# Usuários Liberados para acessar o bot
# Apagar os exemplos e inserir os userID
# Rodar o script e verificar no arquivo de log botTelegram_zabbix.log vai aparecer o userID
# Acessa o Bot e o userID fica gravado no Log 
# Com esta segurança o seu bot fica restrito somente aqueles que você liberou
##########################################

users_liberados = [111111111, 222222222, 333333333]

############################################
# O Bot-Token do exemplo, tem que modificar
############################################

varBotToken = '161080402:AAGah3HIxM9jUr0NX1WmEKX3cJCv9PyWD58'


##########################################

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='botTelegram_zabbix.log')
logging.info('Started')

logger = logging.getLogger(__name__)
job_queue = None


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.


def start(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
	logging.info(chat_id)
        #bot.sendMessage(chat_id, text = 'Comando não reconhecido ou usuário não liberado')
        return
    bot.sendMessage(update.message.chat_id, text='Seja bem vindo!!')


def mapa1(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        return
    try:
        bot.sendMessage(chat_id, text='Aguarde, consulta em execução...')
	urllib.urlretrieve(varZabbixStatus, "botTelegram_mapa1.jpg")
	bot.sendPhoto(chat_id=update.message.chat_id, photo=open('botTelegram_mapa1.jpg', 'rb'))

    except IndexError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return
    except ValueError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return

def mapa2(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        return
    try:
        bot.sendMessage(chat_id, text='Aguarde, consulta em execução...')
	urllib.urlretrieve(varZabbixHidricas, "botTelegram_mapa2.jpg")
	bot.sendPhoto(chat_id=update.message.chat_id, photo=open('botTelegram_mapa2.jpg', 'rb'))

    except IndexError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return
    except ValueError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return

def mapa3(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        return
    try:
        bot.sendMessage(chat_id, text='Aguarde, consulta em execução...')
	urllib.urlretrieve(varZabbixPmuc, "botTelegram_mapa3.jpg")
	bot.sendPhoto(chat_id=update.message.chat_id, photo=open('botTelegram_mapa3.jpg', 'rb'))

    except IndexError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return
    except ValueError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return

def mapa4(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        return
    try:
        bot.sendMessage(chat_id, text='Aguarde, consulta em execução...')
	urllib.urlretrieve(varZabbixScla, "botTelegram_mapa4.jpg")
	bot.sendPhoto(chat_id=update.message.chat_id, photo=open('botTelegram_mapa4.jpg', 'rb'))

    except IndexError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return
    except ValueError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return

def mapa5(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        return
    try:
        bot.sendMessage(chat_id, text='Aguarde, consulta em execução...')
	urllib.urlretrieve(varZabbixScla, "botTelegram_mapa5.jpg")
	bot.sendPhoto(chat_id=update.message.chat_id, photo=open('botTelegram_mapa5.jpg', 'rb'))

    except IndexError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return
    except ValueError:
        #bot.sendMessage(chat_id, text='Comando não reconhecido ou usuário não liberado')
        return

def help(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        #bot.sendMessage(chat_id, text = 'Comando não reconhecido ou usuário não liberado')
        return
    bot.sendMessage(update.message.chat_id, text="Help:\n"
                                                 "/rede1 - Mapa 1\n"
                                                 "/rede2 - Mapa 2\n"
                                                 "/rede3 - Mapa 3\n"
                                                 "/rede4 - Mapa 4\n"
                                                 "/rede5 - Mapa 5\n")

def error(bot, update, error):
    logger.warn('Update "%s" error "%s"' % (update, error))


def main():
    global job_queue

    updater = Updater(varBotToken)
    job_queue = updater.job_queue

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # Voce pode modificar os comandos que estao entre "" e deixar a funcao 

    dp.add_handler(CommandHandler("rede1", mapa1))
    dp.add_handler(CommandHandler("rede2", mapa2))
    dp.add_handler(CommandHandler("rede3", mapa3))
    dp.add_handler(CommandHandler("rede4", mapa4))
    dp.add_handler(CommandHandler("rede5", mapa5))
    dp.addHandler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    logging.info('Finished')
    logging.shutdown()

if __name__ == '__main__':
    main()