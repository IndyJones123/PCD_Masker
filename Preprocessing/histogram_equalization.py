import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    # Menghitung histogram citra
    height, width = image.shape
    histogram = np.zeros(256)

    for i in range(height):
        for j in range(width):
            histogram[image[i, j]] += 1

    return histogram

def histogram_equalization(image_path):
    # Baca citra
    image = cv2.imread(image_path)

    # Konversi citra ke skala abu-abu
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Menghitung histogram citra asli
    hist_original = calculate_histogram(gray_image)

    # Menghitung probabilitas munculnya setiap intensitas piksel
    total_pixels = gray_image.shape[0] * gray_image.shape[1]
    probabilities = hist_original / total_pixels

    # Menghitung kumulatif distribusi
    cdf = np.cumsum(probabilities)

    # Normalisasi intensitas piksel
    eq_image = np.interp(gray_image.flatten(), np.arange(0, 256), np.round(cdf * 255))

    # Hitung histogram citra hasil equalization
    hist_equalized = calculate_histogram(eq_image.astype(np.uint8).reshape(gray_image.shape))

    # Bentuk citra hasil equalization
    equalized_image = eq_image.astype(np.uint8).reshape(gray_image.shape)

    # Menampilkan 4 gambar dalam satu tampilan
    plt.figure(figsize=(12, 12))

    # Tampilkan citra asli
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    # Tampilkan histogram citra asli
    plt.subplot(2, 2, 2)
    plt.plot(hist_original, color='blue')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')
    plt.title('Histogram Asli')
    plt.xlim([0, 256])

    # Tampilkan citra hasil equalization
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Hasil Histogram Equalization')
    plt.axis('off')

    # Tampilkan histogram citra hasil equalization
    plt.subplot(2, 2, 4)
    plt.plot(hist_equalized, color='red')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')
    plt.title('Histogram Equalization')
    plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()

