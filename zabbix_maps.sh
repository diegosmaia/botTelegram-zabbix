#!/bin/bash

##########################################################################
# PHANTOMJS_Zabbix_maps - Envio de MAPS do Zabbix
# Filename: zabbix_maps.sh
# Revision: 1.0
# Date: 06/03/2019
# Author: Diego Maia - diegosmaia@yahoo.com.br Telegram - @diegosmaia
##########################################################################


##############################################
# Conta de usuário
##############################################

USER=155706551
USER=$1

############################################
# O Bot-Token do exemplo, tem que modificar
############################################

BOT_TOKEN='161080402:AAGah3HIxM9jUr0NX1WmEKX3cJCv9PyWD58'


COOKIE="/tmp/cookie-$(date "+%Y.%m.%d-%H.%M.%S")"
PNG_PATH="/tmp/screen_maps-$(date "+%Y.%m.%d-%H.%M.%S").png"



if [ "$#" -lt 1 ]
then
    exit 1
fi

cd /opt/botTelegram_zabbix

echo "Gerando PNG"
./phantomjs --cookies-file=$COOKIE zabbix_maps.js $2 $PNG_PATH

# Upload do screen

echo "Enviando PNG"
curl -k -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendPhoto" -F chat_id="${USER}" -F photo="@${PNG_PATH}"



############################################
# Apagando os arquivos utilizados no script
############################################

rm -f ${COOKIE}
rm -f ${PNG_PATH}
rm -f ${ZABBIXMSG}
exit 0

