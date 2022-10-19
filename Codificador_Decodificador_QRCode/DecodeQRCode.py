from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Guilherme.costa/Documents/myqrcode.png')

resultado = decode(img)

print(resultado)