var ping = require('ping');
var dns = require('dns');
var xl = require('excel4node');


var wb = new xl.Workbook();

var ws = wb.addWorksheet('Sheet 1');
var style = wb.createStyle({
    font: {
        color: '#2793e6',
        size: 12
    },
    numberFormat: '$#,##0.00; ($#,##0.00); -'
});

var count = 0;
var msg;
var hosts = ['192.168.1.1', '8.8.8.8','192.168.1.104'];

function pingIp(ip){
     var out = ping.sys.probe(ip,function(isAlive){
         console.log(isAlive);
     });

      //msg = isAlive ? 'host ' + ip + ' is alive' : 'host ' + ip + ' is dead';

        //return msg;
    }



console.log(pingIp("8.8.8.8"));

//hosts.forEach(function(host){
//
//    ping.sys.probe(host, function(isAlive){
//        count = count + 1;
//        var msg = isAlive ? 'host ' + host + ' is alive' : 'host ' + host + ' is dead';
//        console.log(msg);
//
//        ws.cell(count,1).string(host).style(style);
//        dns.reverse(host,function(err,domains){
//                    if(domains === undefined){
//                        domains = "DNS Unavailable";
//                    }
//                    ws.cell(count,2).string(domains).style(style);
//    				console.log(domains);
//                    wb.write('Excel2.xlsx');
//    			});
//
//    	});
//});
