# botTelegram-zabbix
Telegram Zabbix Bot - Send Network Map




\#############################
Instalar o Python Pip
\#############################


sudo apt-get install python-pip

#############################
Instalar os pacotes python necessários
#############################


pip install -r requirements.txt

#############################
Editar o arquivo botTelegram-zabbix.py
#############################

#############################
Modificar as linhas abaixo
#############################




##########################################
# Abrir o Zabbix ir em monitoramento - > mapas
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

# Verificar o arquivo 
# https://github.com/diegosmaia/zabbix-telegram/blob/master/Zabbix-Telegram-com-graficos.pdf

varBotToken = '161080402:AAGah3HIxM9jUr0NX1WmEKX3cJCv9PyWD58'

############################################
# Variaveis a serem modificadas
############################################

varUsername = "admin"
varPassword = "zabbix"
varZabbixServer = "http://192.168.10.24/zabbix"

# Tela de login está em portugues ou Ingles
# Se for em portugues (PT) vc comenta a linha varZabbixLanguage = "US" com # no início da linha, e descomenta (retira o #) da linha varZabbixLanguage = "PT"

varZabbixLanguage = "US"
# varZabbixLanguage = "PT"


#############################
Para acompanhar as atualizações: 
https://telegram.me/githubdiegosmaia
#############################


https://br.linkedin.com/pub/diego-santos-maia/2b/b60/173
