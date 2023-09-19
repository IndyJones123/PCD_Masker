from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def citra_grayscale(input_image_path):
    # Buka gambar
    CITRA = Image.open(input_image_path)
    width, height = CITRA.size
    
    # Konversi ke array numpy untuk manipulasi lebih lanjut
    image_array = np.array(CITRA)
    
    # Inisialisasi array untuk citra grayscale
    grayscale_array = np.empty((height, width), dtype=np.uint8)
    
    # Iterasi melalui setiap piksel
    for i in range(height):
        for j in range(width):
            # Ambil nilai warna rata-rata sebagai grayscale
            grayscale_value = int(np.mean(image_array[i, j]))
            grayscale_array[i, j] = grayscale_value
    
    # Konversi array grayscale ke objek gambar
    grayscale_image = Image.fromarray(grayscale_array)

    return grayscale_image

# Memanggil fungsi citra_grayscale dengan input path gambar
def perform_grayscale(image_path):
    # Memanggil fungsi citra_grayscale untuk konversi ke citra grayscale
    grayscale_image = citra_grayscale(image_path)

    # Tampilkan gambar asli dan hasil citra grayscale secara berdampingan
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(Image.open(image_path))
    ax[0].set_title('Gambar Asli')

    # Tampilkan hasil citra grayscale
    ax[1].imshow(grayscale_image, cmap='gray')
    ax[1].set_title('Hasil Citra Grayscale')

    # Sembunyikan sumbu
    for a in ax:
        a.axis('off')

    # Tampilkan plot
    plt.show()
