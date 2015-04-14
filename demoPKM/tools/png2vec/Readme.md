# Installation

1. Download [potrace](http://potrace.sourceforge.net/) *Precompiled distributions* corresponding to the system you have.    
2. Download [ImageMagick](http://www.imagemagick.org/script/binary-releases.php)    
3. Now run the following code
 ```r
 pngtovecpdf("./example1.png","~/bin/potrace/potrace","convert")
 ```

# Usage

| | |
|:---|---|
| filename | Png filename |
| potrace.exepath | potrace exe/bin file path |
| imagemaick.exepath | ImageMagick convert exe/bin file path |

# Comparison

The png file uses default DPI setting in R.

Left = before. Right = After (scale=170%)

![COMP](./snapshot1.png)

But the tiny dash grid lines vanishes.



