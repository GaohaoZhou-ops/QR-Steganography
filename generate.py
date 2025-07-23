import qrcode

data = "https://www.google.com"

qr_img = qrcode.make(data)

qr_img.save("my_qrcode.png")