# botTelegram-zabbix
#Telegram Zabbix Bot - Send Network Map

\#############################

Baixar o PhantonJS e extrair na mesma pasta do bot /opt/botTelegram_zabbix
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

\#############################

\#############################

Instalar o Python Pip

\#############################


sudo apt-get install python-pip

\#############################

Instalar os pacotes python necessários

\#############################


pip install -r requirements.txt

\#############################

Editar o arquivo botTelegram-zabbix.py

Modificar as linhas abaixo:

\#############################


Abrir o Zabbix ir em monitoramento - > mapas

Copiar os ID dos mapas que quer receber pelo Telegram

Procurar por estas linhas e modificar o número 1 depois do {} pelo ID do mapa do Zabbix
varSendcameracmd = "/opt/botTelegram_zabbix/zabbix_maps.sh {} 1&" .format(chat_id)



Verificar o pdf abaixo sobre como criar o BOT e conseguir o BotToken

https://github.com/diegosmaia/zabbix-telegram/blob/master/Zabbix-Telegram-com-graficos.pdf

varBotToken = '161080402:AAGah3HIxM9jUr0NX1WmEKX3cJCv9PyWD58'


varUsername = "admin"

varPassword = "zabbix"

varZabbixServer = "http://192.168.10.24/zabbix"

Tela de login está em portugues ou Ingles

Se for em portugues (PT) vc comenta a linha varZabbixLanguage = "US" com # no início da linha, e descomenta (retira o #) da linha 

varZabbixLanguage = "PT"


varZabbixLanguage = "US"


\# varZabbixLanguage = "PT"


\#############################
Modificar nos scripts .JS 

var zabbix = 'http://192.168.10.24/zabbix' ; 
var zabbix_user = 'admin' ; 
var zabbix_password = 'zabbix' ; 

\#############################

\#############################

Para acompanhar as atualizações: 
https://telegram.me/githubdiegosmaia

\#############################


https://br.linkedin.com/pub/diego-santos-maia/2b/b60/173
