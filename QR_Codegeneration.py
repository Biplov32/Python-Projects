import qrcode as qr
from PIL import Image
# img = qr.make('https://www.linkedin.com/in/biplov-belbase/')
# img.save('linkdenqr.jpeg')
qrc = qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4)

qrc.add_data("https://www.linkedin.com/in/biplov-belbase/")
qrc.make(fit=True)


img=qrc.make_image(fill_color="blue",back_color="white")
img.save('linkden2.jpeg')