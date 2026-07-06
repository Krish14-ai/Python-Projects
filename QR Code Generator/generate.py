import qrcode as qr
img = qr.make('Hello')
img.save('hello.png')
