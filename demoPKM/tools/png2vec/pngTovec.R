#/usr/bin/R

potrace.exepath <- "~/bin/potrace/potrace"
potrace.option <- "-b -o"

imagemaick.exepath <- "convert"
imagemaick.option <- "-grayscale Rec709Luma -density 400"

pngfile <- "example1.png"



pngtovecpdf <- function(filename,
						potrace.exepath,
						imagemaick.exepath,
						potrace.option="-b pdf -o",
						imagemaick.option = "-channel RGBA -matte -colorspace gray -density 400"
){
filename = strsplit(pngfile,split=".png")[[1]]
cmd1 = paste(imagemaick.exepath, imagemaick.option,pngfile,
			 paste(filename,'.pnm',sep='')
			 )

cmd2 = paste(potrace.exepath,paste(filename,'.pnm',sep=''),
			 potrace.option, paste(filename,'.pdf',sep=''))

cat("Runing:\n",cmd1,"\n",cmd2,"\n");
system(cmd1)
system(cmd2)
}

pngtovecpdf("./example1.png","~/bin/potrace/potrace","convert")

