import cv2
import numpy as np

def perform_zoom(image_path, zoom_factor):
    # Baca gambar
    image = cv2.imread(image_path)

    # Periksa apakah gambar berhasil dimuat
    if image is not None:
        # Dapatkan dimensi gambar
        height, width, channels = image.shape

        # Hitung ukuran gambar yang baru setelah zoom
        new_height = int(height * zoom_factor)
        new_width = int(width * zoom_factor)

        # Buat gambar baru dengan ukuran yang baru
        zoomed_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

        # Faktor scaling untuk mendapatkan koordinat dari gambar asli
        scale_x = width / new_width
        scale_y = height / new_height

        for y in range(new_height):
            for x in range(new_width):
                original_x = int(x * scale_x)
                original_y = int(y * scale_y)

                # Pastikan koordinat berada dalam batas gambar asli
                original_x = max(0, min(original_x, width - 1))
                original_y = max(0, min(original_y, height - 1))

                zoomed_image[y, x] = image[original_y, original_x]

        # Tampilkan gambar asli dan gambar yang di-zoom
        cv2.imshow("Gambar Asli", image)
        cv2.imshow("Gambar yang Di-zoom", zoomed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Gagal memuat gambar.")

# Contoh penggunaan:
# Untuk melakukan zoom in (perbesar) gambar dengan faktor 2:
perform_zoom("gambar.jpg", 2.0)

# Untuk melakukan zoom out (perkecil) gambar dengan faktor 0.5:
# perform_zoom("gambar.jpg", 0.5)
