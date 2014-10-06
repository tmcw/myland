import rasterio, os, glob, numpy, pickle, sys, itertools

from itertools import izip, chain, repeat

# hella simple(istic) technique for extracting moving objects
# from a video given as a series of frames.
#
# basically:
#
#     for each ten frames,
#         take the median of those ten frames together
#         for each frame,
#             find the difference between that frame and the median

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

def z1(arr):
    if arr.max() == 0: return arr
    arr *= (1.0/arr.max())
    return arr

def flip(arr):
    arr = z1(numpy.maximum(numpy.minimum(arr * 2.0, twofifty), z))
    return arr

i = 0
j = 0
captures = glob.glob('captures/*.jpg')

groups = grouper(5, captures)

with rasterio.drivers():
    for group in groups:
        b_every = []
        g_every = []
        r_every = []
        for f in group:
            with rasterio.open(f) as src:
                b, g, r = src.read()
                b_every.append(b);
                g_every.append(g);
                r_every.append(r);

        bmed = normalize(numpy.median(b_every, 0));
        gmed = normalize(numpy.median(g_every, 0));
        rmed = normalize(numpy.median(r_every, 0));

        for f in group:
            i = i + 1
            with rasterio.open(f) as src:
                b, g, r = src.read()
                b_compare = normalize(b)
                g_compare = normalize(g)
                r_compare = normalize(r)

                bdif = numpy.multiply(b_compare, flip(numpy.absolute(numpy.subtract(b_compare.astype(int), bmed.astype(int)))))
                gdif = numpy.multiply(g_compare, flip(numpy.absolute(numpy.subtract(g_compare.astype(int), gmed.astype(int)))))
                rdif = numpy.multiply(r_compare, flip(numpy.absolute(numpy.subtract(r_compare.astype(int), rmed.astype(int)))))

                with rasterio.open('trackers/%06d.tif' % i, 'w', driver='GTiff',
                        width=352, height=240, count=3, dtype=rasterio.uint8) as dst:
                    dst.write_band(1, bdif.astype(rasterio.uint8))
                    dst.write_band(2, gdif.astype(rasterio.uint8))
                    dst.write_band(3, rdif.astype(rasterio.uint8))
