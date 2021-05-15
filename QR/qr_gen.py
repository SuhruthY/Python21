import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = input("Enter the URL:")

if len(s) <= 1: s = "https://suhruthy.github.io/SuhruthY/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("WhYblog.svg", scale=8)