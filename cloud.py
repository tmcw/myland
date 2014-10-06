import rasterio, os, glob, numpy, pickle

with rasterio.drivers():
    b_every = []
    g_every = []
    r_every = []
    if True:
        print "collecting"
        i = 0
        for f in glob.glob('captures/*.jpg'):
            i = i + 1
            if i < 10000:
                print "%d done" % i
                try:
                    with rasterio.open(f) as src:
                        b, g, r = src.read()
                        b_every.append(b);
                        g_every.append(g);
                        r_every.append(r);
                except Exception, e:
                    print e

        pickle.dump(b_every, open('b.dump', 'w'))
        pickle.dump(g_every, open('g.dump', 'w'))
        pickle.dump(r_every, open('r.dump', 'w'))
    else:
        b_every = pickle.load(open('b.dump'))
        g_every = pickle.load(open('g.dump'))
        r_every = pickle.load(open('r.dump'))

    print "computing max"
    bmax = numpy.max(b_every, 0);
    gmax = numpy.max(g_every, 0);
    rmax = numpy.max(r_every, 0);

    print "computing min"
    bmin = numpy.min(b_every, 0);
    gmin = numpy.min(g_every, 0);
    rmin = numpy.min(r_every, 0);

    print "computing median"
    bmed = numpy.median(b_every, 0);
    gmed = numpy.median(g_every, 0);
    rmed = numpy.median(r_every, 0);
    print "writing"

    with rasterio.open('max.tif', 'w', driver='GTiff',
            width=352, height=240, count=3, dtype=rasterio.uint8) as dst:
        dst.write_band(1, bmax.astype(rasterio.uint8))
        dst.write_band(2, gmax.astype(rasterio.uint8))
        dst.write_band(3, rmax.astype(rasterio.uint8))

    with rasterio.open('median.tif', 'w', driver='GTiff',
            width=352, height=240, count=3, dtype=rasterio.uint8) as dst:
        dst.write_band(1, bmed.astype(rasterio.uint8))
        dst.write_band(2, gmed.astype(rasterio.uint8))
        dst.write_band(3, rmed.astype(rasterio.uint8))

    with rasterio.open('min.tif', 'w', driver='GTiff',
            width=352, height=240, count=3, dtype=rasterio.uint8) as dst:
        dst.write_band(1, bmin.astype(rasterio.uint8))
        dst.write_band(2, gmin.astype(rasterio.uint8))
        dst.write_band(3, rmin.astype(rasterio.uint8))
