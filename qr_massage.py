import qrcode

url = "https://dikidi.net/269997"

# Создание QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Создание изображения
img = qr.make_image(fill_color='white', back_color='blue')

# Сохранение изображения
img.save("tlm43.png")

