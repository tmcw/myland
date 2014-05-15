var http = require('http'),
    concat = require('concat-stream'),
    fs = require('fs'),
    xml2js = require('xml2js');

http.get('http://trafficland.com/data/data.xml?swlat=-90&swlng=-180&nelat=90&nelng=180' +
    '&system=pub&pubtoken=2c66cb0f7eadc054ff2c16c4d9713d40', loaded);
// dataToGeoJSON(require('./data.json'));

function loaded(res) {
    res.pipe(concat(processXML));
}

function processXML(buf) {
    xml2js.parseString(buf.toString(), function(err, result) {
        fs.writeFileSync('data.json', JSON.stringify(result));
        dataToGeoJSON(result);
    });
}

function dataToGeoJSON(data) {
    var fc = { type: 'FeatureCollection', features: [] };
    data.cameras.camera.forEach(function(camera) {
        fc.features.push({
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: [
                    +camera.$.lng,
                    +camera.$.lat
                ]
            },
            properties: camera.$
        });
    });
    fs.writeFileSync('cameras.geojson', JSON.stringify(fc, null, 2));
}
