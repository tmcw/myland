# myland

![](https://farm8.staticflickr.com/7336/14002354999_6328735cb8_h.jpg)

Scraping and displaying [TrafficLand](http://www.trafficland.com/) data.

TrafficLand sets up [public-private partnerships](http://en.wikipedia.org/wiki/Public%E2%80%93private_partnership) with
local governments to install cameras on your stoplights and so on.

## Images

See [images on TrafficLand's site](http://trafficland.com/city/WAS/index.html). The image
feeds have API-like URLs but require a key that's probably a timestamp combined
with some private key.

## data

* `data.json` is the raw data processed from data.xml
* `cameras.geojson` is that data turned into geojson

## install

    npm install

## run

    node index.js
