var fs = require('fs'),
  http = require('http');

var URL = 'http://ie.trafficland.com/200013/full?system=ddot&pubtoken=defd73dd750050992f058c40d231efdabe7&t=1412254287091';

setInterval(snap, 1000 * 5);

function snap() {
  try {
    http
      .get(URL, function(resp) {
        resp.pipe(fs.createWriteStream('./captures/' + Date.now() + '.jpg'));
      }).on('error', function(err) {
        console.error(err);
      });
  } catch(e) {
    console.error('exception', e);
  }
}
