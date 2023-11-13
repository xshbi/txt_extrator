import cv2
import pytesseract
from pytesseract import Output
import PIL.Image



myconfig = r"--psm 11 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("ss.png"),config=myconfig)
with open("tdet.txt","wt") as f:
    print("The detected is  : ",text,file=f)