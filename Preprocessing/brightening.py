from PIL import Image
import os
import matplotlib.pyplot as plt

def clipping(intensitas):
    if intensitas < 0:
        return 0
    if intensitas > 255:
        return 255
    return intensitas

def atur_pencerahan(nilai_pencerahan, input_image_path):
    # Buka gambar
    CITRA = Image.open(input_image_path)
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = clipping(PIXEL[x, y][0] + nilai_pencerahan)
            G = clipping(PIXEL[x, y][1] + nilai_pencerahan)
            B = clipping(PIXEL[x, y][2] + nilai_pencerahan)
            PIXEL[x, y] = (R, G, B)

    return CITRA

# Fungsi untuk menampilkan gambar asli dan hasil pencerahan
def tampilkan_hasil_pencerahan(input_image_path, nilai_pencerahan):
    # Tampilkan gambar asli dan hasil pencerahan secara berdampingan
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Simpan hasil citra dengan peningkatan intensitas
    hasil_citra = atur_pencerahan(nilai_pencerahan, input_image_path)

    # Tampilkan gambar asli
    axs[0].imshow(Image.open(input_image_path))
    axs[0].set_title('Gambar Asli')

    # Tampilkan hasil citra dicerahkan
    axs[1].imshow(hasil_citra)
    axs[1].set_title('Gambar Dicerahkan')

    # Sembunyikan sumbu
    axs[0].axis('off')
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()
