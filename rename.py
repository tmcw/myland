import os, glob

# Tiny Python script to rename date-named files
# to sequential numbers for ffmpeg. Probably
# doable in bash, but my bash sucks.

i = 0
for f in os.listdir('.'):
    if f.endswith('jpg'):
        x = i / 10
        os.rename(f, '%06d.jpg' % x)
        i = i + 1
