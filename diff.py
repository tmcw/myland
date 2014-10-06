import rasterio, os, glob, numpy, pickle, sys, itertools

from itertools import izip, chain, repeat

z = numpy.zeros((240, 352))
twofifty = numpy.zeros((240, 352))
twofifty.fill(255.0)

def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip(*[chain(iterable, repeat(padvalue, n-1))]*n)

def normalize(arr):
    if arr.max() == 0: return arr
    arr *= (255.0/arr.max())
    return arr

def flip(arr):
    arr = normalize(numpy.minimum(285.0 - arr, twofifty))
    print arr
    return arr

i = 0
j = 0
captures = glob.glob('captures/*.jpg')

groups = grouper(5, captures)

with rasterio.drivers():
    for group in groups:
        for f in group:
            print "med %s" % f
            b_every = []
            g_every = []
            r_every = []
            with rasterio.open(f) as src:
                b, g, r = src.read()
                b_every.append(b);
                g_every.append(g);
                r_every.append(r);

        bmed = normalize(numpy.median(numpy.array(b_every), axis=0));
        gmed = normalize(numpy.median(numpy.array(g_every), axis=0));
        rmed = normalize(numpy.median(numpy.array(r_every), axis=0));

        for f in group:
            print "gro %s" % f
            print f
            i = i + 1
            if i % 5 != 0:
                j = j + 1
                with rasterio.open(f) as src:
                    print src.shape
                    b, g, r = src.read()
                    b_compare = normalize(b)
                    g_compare = normalize(g)
                    r_compare = normalize(r)

                    bdif = flip(normalize(numpy.absolute(numpy.subtract(b_compare.astype(int), bmed.astype(int)))))
                    gdif = flip(normalize(numpy.absolute(numpy.subtract(g_compare.astype(int), gmed.astype(int)))))
                    rdif = flip(normalize(numpy.absolute(numpy.subtract(r_compare.astype(int), rmed.astype(int)))))

                    with rasterio.open('trackers/%06d.tif' % j, 'w', driver='GTiff',
                            width=352, height=240, count=3, dtype=rasterio.uint8) as dst:
                        dst.write_band(1, bdif.astype(rasterio.uint8))
                        dst.write_band(2, gdif.astype(rasterio.uint8))
                        dst.write_band(3, rdif.astype(rasterio.uint8))
