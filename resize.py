import os, sys
from PIL import Image

inputdir = sys.argv[1]
rate = float(sys.argv[2])
outputdir = "thumbnails"

print("Directory: ", inputdir)
print("Resize rate: ", rate)

os.mkdir(outputdir)

for filename in os.listdir(inputdir):
    f, e = os.path.splitext(filename)
    try:
        im = Image.open(inputdir + filename)
        print(im.size)
        im.thumbnail((int(im.size[0] * rate), int(im.size[1] * rate)))
        print(im.size)
        im.save(outputdir + "/" + filename, "JPEG")
    except IOError:
        print("cannot create thumbnail for", infile)
