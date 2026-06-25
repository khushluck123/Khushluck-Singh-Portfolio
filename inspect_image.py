from PIL import Image
import os
import sys

path = os.path.join(os.getcwd(), 'hero image.png')
print('PATH', path)
img = Image.open(path)
print('SIZE', img.size)
print('MODE', img.mode)

try:
    import pytesseract
    text = pytesseract.image_to_string(img)
    print('OCR_START')
    print(text)
    print('OCR_END')
except Exception as e:
    print('OCR_ERROR', repr(e))
