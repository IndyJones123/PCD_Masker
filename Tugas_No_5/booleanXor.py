from PIL import Image

# Membaca dua citra menggunakan PIL (Python Imaging Library)
image1 = Image.open('mask.jpg')
image2 = Image.open('noMasker.jpg')

# Pastikan kedua citra memiliki ukuran yang sama
if image1.size == image2.size:
    # Mengambil data piksel dari citra sebagai array
    pixels1 = list(image1.getdata())
    pixels2 = list(image2.getdata())

    # Menggunakan operasi xor bitwise
    hasil_xor = [tuple(p1 ^ p2 for p1, p2 in zip(pixel1, pixel2)) for pixel1, pixel2 in zip(pixels1, pixels2)]

    # Membuat citra hasil dari array piksel yang telah diolah
    hasil_image_xor = Image.new('RGB', image1.size)
    hasil_image_xor.putdata(hasil_xor)

    # Menyimpan citra hasil operasi or ke dalam file
    hasil_image_xor.save('xor_citra.jpg')
else:
    print("Ukuran citra tidak sama, operasi boolean tidak dapat dilakukan.")
