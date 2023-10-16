import numpy as np
import cv2

# Membaca citra
img = cv2.imread('Gambar2.jpg', 0)  # Mode 0 untuk citra grayscale

# Membuat kernel filter rata-rata 3x3
kernel = np.ones((3, 3), np.float32) / 6

# Menggunakan filter lowpass
filtered_img = cv2.filter2D(img, -1, kernel)

# Menampilkan citra asli dan hasil filter
cv2.imshow('Citra Asli', img)
cv2.imshow('Hasil Filter Lowpass', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
