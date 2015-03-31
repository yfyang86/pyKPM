#!/bin/sh

sudo apt-get install cdrdao bchunk
toc2cue $1.toc $1.cue
bchunk -s -w $1.bin $1.cue $1
