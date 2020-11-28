import urllib.request
from fpdf import FPDF
import cv2
import numpy

i = 1

# create a new pdf
pdf = FPDF()

# until theres an error
while True:
    if i > 10: break
    try:
        pdf.add_page()

        fname = f"img{i}.jpg"
        url = f"https://content.wdl.org/10096/service/thumbnail/1431369762/1024x1024/1/{i}.jpg"

        urllib.request.urlretrieve(url, fname)

        pdf.image(fname, type="jpg")

        i += 1

    except:
        break

# write to the pdf
pdf.output("florentine.pdf")
