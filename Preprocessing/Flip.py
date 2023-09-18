import cv2
import numpy as np

def perform_flip(image_path, flip_direction):
    # Baca gambar
    image = cv2.imread(image_path)

    # Periksa apakah gambar berhasil dimuat
    if image is not None:
        # Dapatkan dimensi gambar
        height, width, channels = image.shape

        # Buat kanvas kosong dengan ukuran yang sama dengan gambar asli
        flipped_image = np.zeros((height, width, channels), dtype=np.uint8)

        if flip_direction == 0:
            # Melakukan flip gambar secara horizontal secara manual
            for y in range(height):
                for x in range(width):
                    flipped_image[y, width - 1 - x] = image[y, x]
        elif flip_direction == 1:
            # Melakukan flip gambar secara vertikal secara manual
            for y in range(height):
                for x in range(width):
                    flipped_image[height - 1 - y, x] = image[y, x]
        else:
            print("Arah flip tidak valid. Gunakan 'horizontal' atau 'vertical'.")
            return

        # Tampilkan gambar asli dan gambar yang diflip
        cv2.imshow("Gambar Asli", image)
        cv2.imshow("Gambar yang Diflip", flipped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Gagal memuat gambar.")

# Contoh penggunaan:
# Untuk melakukan flip gambar secara horizontal:
# perform_flip("Gambar.jpg", "horizontal")

# Untuk melakukan flip gambar secara vertikal:
# perform_flip("gambar.jpg", "vertical")
