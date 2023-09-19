# negatif_image.py

from PIL import Image
import matplotlib.pyplot as plt

def ubah_gambar_negatif(input_image_path):
    # Load gambar
    CITRA = Image.open(input_image_path)

    # Mendapatkan ukuran gambar
    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    # Salin gambar asli
    CITRA_ASLI = CITRA.copy()

    # Load pixel
    PIXEL = CITRA.load()

    # Mengubah gambar menjadi negatif
    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = 255 - PIXEL[x, y][0]
            G = 255 - PIXEL[x, y][1]
            B = 255 - PIXEL[x, y][2]
            PIXEL[x, y] = (R, G, B)

    # Tampilkan gambar asli dan hasil negatif secara berdampingan
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(CITRA_ASLI)
    ax[0].set_title('Gambar Asli')

    # Tampilkan hasil negatif
    ax[1].imshow(CITRA)
    ax[1].set_title('Hasil Gambar Negatif')

    # Sembunyikan sumbu
    for a in ax:
        a.axis('off')

    # Tampilkan plot
    plt.show()
