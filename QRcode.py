import qrcode
qr_image = qrcode.make("Hello!! how are you....")
qr_image.save("hello_qr_code.png")