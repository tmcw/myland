import rasterio, os, glob, numpy, pickle, sys

with rasterio.drivers():

    b_compare = []
    g_compare = []
    r_compare = []

    b_every = []
    g_every = []
    r_every = []

    with rasterio.open(sys.argv[1]) as src:
        print src.shape
        b, g, r = src.read()
        b_every.append(b);
        g_every.append(g);
        r_every.append(r);
        print "computing median"
        less = numpy.array(src.shape)
        less.fill(min(b_every))
        b_every = b_every - less
        print b_every
        print "writing"

    # with rasterio.open('difference.tif', 'w', driver='GTiff',
    #         width=352, height=240, count=3, dtype=rasterio.uint8) as dst:
    #     print bdif.astype(rasterio.uint8).shape
    #     dst.write_band(1, bdif.astype(rasterio.uint8)[0])
    #     dst.write_band(2, gdif.astype(rasterio.uint8)[0])
    #     dst.write_band(3, rdif.astype(rasterio.uint8)[0])
