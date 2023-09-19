from PIL import Image

def boolean_xor(image1, image2):
    IMAGE1 = Image.open(image1)
    IMAGE2 = Image.open(image2)
# Pastikan kedua citra memiliki ukuran yang sama
    if IMAGE1.size == IMAGE2.size:
        # Membuat objek citra hasil yang akan dihasilkan
        hasil_image_xor = Image.new('RGB', IMAGE1.size)

        # Mendapatkan objek piksel untuk setiap citra
        pixels1 = IMAGE1.load()
        pixels2 = IMAGE2.load()
        hasil_pixels = hasil_image_xor.load()

        # Melakukan operasi xor bitwise pada setiap piksel
        for x in range(IMAGE1.width):
            for y in range(IMAGE1.height):
                r1, g1, b1 = pixels1[x, y]
                r2, g2, b2 = pixels2[x, y]

                hasil_r = r1 ^ r2
                hasil_g = g1 ^ g2
                hasil_b = b1 ^ b2

                hasil_pixels[x, y] = (hasil_r, hasil_g, hasil_b)

        # Menampilkan citra hasil operasi xor
        hasil_image_xor.show()
    else:
        print("Ukuran citra tidak sama, operasi boolean tidak dapat dilakukan.")
