from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Usuario/Documents/myqrcode.png')

resultado = decode(img)

print(resultado)