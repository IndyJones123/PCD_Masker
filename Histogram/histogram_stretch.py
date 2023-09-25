from PIL import Image
import matplotlib.pyplot as plt

def calculate_histogram(image):
    # Inisialisasi histogram
    histogram = [0] * 256
    
    # Dapatkan ukuran gambar
    width, height = image.size
    
    # Loop melalui setiap piksel dan tambahkan ke histogram
    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            histogram[pixel_value] += 1
    
    return histogram

def stretch_histogram(image, histogram):
    # Temukan nilai piksel minimum dan maksimum dalam histogram
    min_value = 0
    max_value = 255
    
    while histogram[min_value] == 0:
        min_value += 1
    
    while histogram[max_value] == 0:
        max_value -= 1
    
    # Hitung faktor scaling
    scale_factor = 255 / (max_value - min_value)
    
    # Lakukan stretching histogram
    width, height = image.size
    stretched_image = Image.new('L', (width, height))
    
    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            new_pixel_value = int((pixel_value - min_value) * scale_factor)
            stretched_image.putpixel((x, y), new_pixel_value)
    
    return stretched_image

def plot_histogram(image_path):
    # Baca citra dengan PIL
    # image = Image.open(image_path).convert('L')  # Konversi ke citra grayscale
    # print(image)
    # Hitung histogram
    histogram = calculate_histogram(image_path)

    # Gambar histogram citra grayscale
    plt.figure(figsize=(12, 6))

    plt.subplot(231)
    plt.title('Histogram Grayscale')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    plt.xlim(0, 255)
    plt.plot(range(256), histogram, color='gray')

    # Tampilkan citra asli
    plt.subplot(232)
    plt.title('Citra Asli')
    plt.imshow(image_path, cmap='gray')
    plt.axis('off')

    # Tampilkan histogram citra grayscale yang telah di-stretching
    plt.subplot(233)
    plt.title('Histogram Grayscale Setelah Stretching')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    plt.xlim(0, 255)

    # Stretch histogram
    stretched_image = stretch_histogram(image_path, histogram)
    stretched_histogram = calculate_histogram(stretched_image)

    plt.plot(range(256), stretched_histogram, color='gray')

    # Tampilkan citra hasil stretching
    plt.subplot(235)
    plt.title('Citra Setelah Stretching')
    plt.imshow(stretched_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# image_path = input("Masukkan Path Gambar: ")
# plot_histogram(image_path)