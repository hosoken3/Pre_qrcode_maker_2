```python
import qrcode

def generate_qrcode(data, filename="qrcode.png"):
 """Generates a QR code image.

 Args:
 data: The data to encode in the QR code (string).
 filename: The name of the output image file (default: "qrcode.png").
 """
 qr = qrcode.QRCode(
 version=1, # Adjust version for size (1-40)
 error_correction=qrcode.constants.ERROR_CORRECT_L, # Error correction level
 box_size=10, # Size of each box in pixels
 border=4, # Border width
 )
 qr.add_data(data)
 qr.make(fit=True)

 img = qr.make_image(fill_color="black", back_color="white")
 img.save(filename)

if __name__ == "__main__":
 data = input("Enter the data to encode in the QR code: ")
 generate_qrcode(data)
 print(f"QR code generated successfully as qrcode.png")

```
