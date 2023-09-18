import numpy as np
import cv2

def perform_rotation(image_path, angle_degrees):
    # Membaca gambar
    image = cv2.imread(image_path)

    # Memeriksa apakah gambar berhasil dimuat
    if image is not None:
        # Mengonversi gambar menjadi larik NumPy
        image_array = np.array(image)

        # Mendapatkan tinggi dan lebar gambar
        height, width, channels = image_array.shape

        # Mengonversi sudut ke dalam radian
        angle_radians = np.deg2rad(angle_degrees)

        # Menghitung dimensi baru gambar untuk menyesuaikan gambar yang sudah dirotasi
        new_width = int(np.round(width * abs(np.cos(angle_radians)) + height * abs(np.sin(angle_radians))))
        new_height = int(np.round(width * abs(np.sin(angle_radians)) + height * abs(np.cos(angle_radians))))

        # Membuat kanvas kosong untuk gambar yang sudah dirotasi
        rotated_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

        # Menghitung pusat gambar asli
        center_x = width // 2
        center_y = height // 2

        # Melakukan rotasi dengan mengulang setiap piksel
        for y in range(new_height):
            for x in range(new_width):
                # Menghitung koordinat pada gambar asli
                original_x = int((x - new_width / 2) * np.cos(angle_radians) -
                                  (y - new_height / 2) * np.sin(angle_radians) + center_x)
                original_y = int((x - new_width / 2) * np.sin(angle_radians) +
                                  (y - new_height / 2) * np.cos(angle_radians) + center_y)

                # Memeriksa apakah koordinat asli berada dalam batas
                if 0 <= original_x < width and 0 <= original_y < height:
                    rotated_image[y, x] = image_array[original_y, original_x]

        # Menampilkan gambar asli dan gambar yang sudah dirotasi
        cv2.imshow("Gambar Asli", image_array)
        cv2.imshow("Gambar yang Sudah Dirotasi", rotated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Gagal memuat gambar.")
