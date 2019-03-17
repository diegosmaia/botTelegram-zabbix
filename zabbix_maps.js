var page = require('webpage').create();
var zabbix = 'http://192.168.10.24/zabbix' ; 
var zabbix_user = 'admin' ; 
var zabbix_password = 'zabbix' ; 
var pageWidth = 1400 ; 
var pageHeight = 900 ; 
var args = require('system').args;
if (args.length == 2) {
    console.log('Informe o ID e o nome do arquivo.png');
    phantom.exit();
}

var sysmapid = args[1];
var namepng = args[2];

page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';
page.viewportSize = {width: pageWidth, height: pageHeight};
//page.zoomFactor = 0.25;

// authorization
	
console.log("Login in Zabbix");
var auth = require ( 'webpage' ).create (), server = zabbix + '/index.php?' , data = 'name=' + zabbix_user + '&password=' + zabbix_password + '&enter=Sign + in' ;     

page.open(server , 'post' , data, function(status) {
    if (status === "success") { 
	page.open(zabbix + '/zabbix.php?action=map.view&sysmapid='+ sysmapid , function(status) {
        window.setTimeout(function() {
 	 	page.render(namepng);
                phantom.exit();
        	}, 5000);
    	});
    }
});




