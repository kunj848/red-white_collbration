import qrcode

# Jis link ya text ka QR banana hai
data = "https://github.com/sufiyan1997-bot/python"

print("Generating QR Code...")
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Image banana aur save karna
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("Success! 'my_qrcode.png' file aapke folder mein save ho gayi hai.")
