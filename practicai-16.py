import qrcode
import barcode
from barcode.writer import ImageWriter

qr = qrcode.make("Joy Sen")
qr.save("joy_qr.png")

code = barcode.get(
    "code128",
    "1234567890",
    writer=ImageWriter()
)

code.save("joy_barcode")

print("QR Code and Barcode Created")