# myland

[![Greenkeeper badge](https://badges.greenkeeper.io/tmcw/myland.svg)](https://greenkeeper.io/)

![](https://farm8.staticflickr.com/7336/14002354999_6328735cb8_h.jpg)

Scraping and displaying [TrafficLand](http://www.trafficland.com/) data.

TrafficLand sets up [public-private partnerships](http://en.wikipedia.org/wiki/Public%E2%80%93private_partnership) with
local governments to use cameras on stoplights for traffic and other sorts
of tasks.

## Images

See [images on TrafficLand's site](http://trafficland.com/city/WAS/). The image
feeds have API-like URLs but require a key that's probably a timestamp combined
with some private key.

## Video

After grabbing stills as JPEG, generate videos with ffmpeg:

ffmpeg -i %06d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4

## data

* `data.json` is the raw data processed from data.xml
* `cameras.geojson` is that data turned into geojson

## install

    npm install

## run

    node index.js
