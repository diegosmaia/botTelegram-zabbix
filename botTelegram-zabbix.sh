#! /usr/bin/env bash
# Para ser executado caso o servidor reinicie
# Adicionar no /etc/rc.local
# sh /opt/botTelegram-zabbix/botTelegram-zabbix.sh

cd /opt/botTelegram-zabbix
python /opt/botTelegram-zabbix/botTelegram-zabbix.py &
exit 0


