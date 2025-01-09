import qrcode
from PIL import Image

qr = qrcode.QRCode(version=5,
box_size=10,
border=2)

data = "https://www.linkedin.com/in/mfurkankarakus/"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color ="white")
img.save("qr.png")