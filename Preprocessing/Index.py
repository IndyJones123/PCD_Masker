<<<<<<< Updated upstream
def option_1():
    print("Option 1 selected. You can put your code here.")
=======
import os;
import Translation;
import Flip;
import Zooming;
from image_negative import ubah_gambar_negatif;
from Grayscale import perform_grayscale;
from brightening import tampilkan_hasil_pencerahan

def option_1():
    print("Option 1 selected.")
    
    # Meminta pengguna untuk memasukkan path gambar untuk konversi ke negatif
    input_image_path = input("Masukkan Path Gambar untuk konversi ke negatif: ")
    
    # Memeriksa apakah file gambar ada di path yang dimasukkan pengguna
    if not os.path.isfile(input_image_path):
        print("File tidak ditemukan.")
        return
    
    # Panggil fungsi ubah_gambar_negatif untuk menampilkan citra negatif
    ubah_gambar_negatif(input_image_path)
>>>>>>> Stashed changes

def option_2():
    print("Option 2 selected.")

    # Meminta pengguna untuk memasukkan path gambar untuk konversi ke grayscale
    input_image_path = input("Masukkan Path Gambar untuk konversi ke grayscale: ")

    # Memeriksa apakah file gambar ada di path yang dimasukkan pengguna
    if not os.path.isfile(input_image_path):
        print("File tidak ditemukan.")
        return

    # Panggil fungsi perform_grayscale untuk menampilkan citra grayscale
    perform_grayscale(input_image_path)

def option_3():
    print("Option 3 selected.")

    # Meminta pengguna memasukkan nama file gambar
    input_image_path = input("Masukkan path gambar : ")

    # Memeriksa apakah file gambar ada di path yang dimasukkan pengguna
    if not os.path.isfile(input_image_path):
        print("File tidak ditemukan.")
    else:
        # Meminta pengguna memasukkan nilai pencerahan
        nilai_pencerahan = int(input("Masukkan nilai pencerahan: "))

        # Panggil fungsi tampilkan_hasil_pencerahan
        tampilkan_hasil_pencerahan(input_image_path, nilai_pencerahan)

def option_4():
    print("Option 4 selected. You can put your code here.")

def option_5():
    print("Option 4 selected. You can put your code here.")

def option_6():
    print("Option 4 selected. You can put your code here.")



def main():
    while True:
        print("\nMenu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Option 5")
        print("6. Option 6")
        print("7. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '4':
            option_4()
        elif choice == '5':
            option_5()
        elif choice == '6':
            option_6()          
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


# import cv2
# import numpy as np

# # Input your image file path
# image_path = "Gambar.jpg"

# # Read the image
# image = cv2.imread(image_path)

# # Check if the image was loaded successfully
# if image is not None:
#     # Convert the image to a NumPy array
#     image_array = np.array(image)

#     tx = -50  # Adjust this vx  alue as needed for your translation in the x-direction
#     ty = 30  # Adjust this value as needed for your translation in the y-direction

#     # Create an empty canvas with the same size as the original image
#     height, width, channels = image.shape
#     translated_image = np.zeros((height, width, channels), dtype=np.uint8)

#     # Iterate through each pixel and copy it to the translated position
#     for y in range(height):
#         for x in range(width):
#             new_x = x + tx
#             new_y = y + ty

#             if 0 <= new_x < width and 0 <= new_y < height:
#                 translated_image[new_y, new_x] = image[y, x]

#     # Display the original and translated images
#     cv2.imshow("Original Image", image)
#     cv2.imshow("Hasil Operasi Translasi Image", translated_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Failed to load the image.")
