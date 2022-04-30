import numpy
from PIL import Image, ImageFilter 
import os

    
def getROIImage(image_path):
    
    if os.path.isfile(image_path):
        imageob = Image.open(image_path).convert('RGB')
        width, height = imageob.size
        pix=imageob.load()
        for i in range(width):
            for j in range(height):
                col=pix[i,j]
                R=col[0]
                G=col[1]
                B=col[2]
                Cb=-0.169 * R - 0.332 * G + 0.500 * B + 128
                Cr=0.500 * R - 0.419 * G - 0.081 * B + 128
                if (Cr > 137 and Cr < 177):
                    if (Cb < 127 and Cb > 77):
                        t = Cb + 0.6 * Cr
                        if (t > 190 and t < 215):
                            pix[i,j]=(255,255,255)
                        else:
                            pix[i,j]=(0,0,0)
                    else:
                        pix[i,j]=(0,0,0)
                else:
                    pix[i,j]=(0,0,0)
        return imageob
            

                  
    