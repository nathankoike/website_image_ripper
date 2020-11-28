import urllib.request
from fpdf import FPDF
import cv2
import numpy

# current page number (not an index)
i = 1

# create a new pdf
pdf = FPDF('P', "pt", (800, 1024))

# until theres an error
while True:
    # until theres an error
    try:
        # add a new page in the pdf
        pdf.add_page(orientation='P')

        # set the filename and the url
        fname = f"img{i}.jpg"
        url = f"https://content.wdl.org/10096/service/thumbnail/1431369762/1024x1024/1/{i}.jpg"

        # fetch the image from the url and save it so we can add it to the pdf
        urllib.request.urlretrieve(url, fname)

        # add the image to the pdf
        pdf.image(fname, type="jpg", x=0, y=0)

        # move on to the next image
        i += 1

    # if theres an error er can end
    except:
        break

# write to the pdf
pdf.output("florentine.pdf")
