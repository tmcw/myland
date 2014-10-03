import os, glob

# Tiny Python script to rename date-named files
# to sequential numbers for ffmpeg. Probably
# doable in bash, but my bash sucks.

i = 0
for f in os.listdir('.'):
    if f.endswith('jpg'):
        os.rename(f, '%06d.jpg' % i)
        i = i + 1
