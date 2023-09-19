import os;
import Translation;
import Rotation;
import Flip;
import Zooming;
import penjumlahan;
import pengurangan;
import booleanAnd;
import booleanOr;
import booleanXor;
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


def option_1():
    print("Option 1 selected.")
      
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
    print("1.Penjumlahan")
    print("2.Pengurangan\n")

    choiceAritmatika = input("Masukan No Pilihan Operasi : ")
    #penjumlahan
    if choiceAritmatika == '1':
        image1_path = input("Masukkan Path Gambar 1: ")
        image2_path = input("Masukkan Path Gambar 2: ")
        penjumlahan.penambahan_dua_citra(image1_path, image2_path)

    #pengurangan
    elif choiceAritmatika == '2':
        image1_path = input("Masukkan Path Gambar 1: ")
        image2_path = input("Masukkan Path Gambar 2: ")
        pengurangan.pengurangan_dua_citra(image1_path, image2_path)
    
    else:
        print("Invalid choice. Please choose a valid option.")


def option_5():
    print("1.Boolean And")
    print("2.Boolean Or")
    print("3.Boolean Xor\n")

    choiceBoolean = input("Masukan No Pilihan Operasi : ")
    #Boolean And
    if choiceBoolean == '1':
        image1_path = input("Masukkan Path Gambar 1: ")
        image2_path = input("Masukkan Path Gambar 2: ")
        booleanAnd.boolean_and(image1_path, image2_path)

    #Boolean Or
    elif choiceBoolean == '2':
        image1_path = input("Masukkan Path Gambar 1: ")
        image2_path = input("Masukkan Path Gambar 2: ")
        booleanOr.boolean_or(image1_path, image2_path)

    #Boolean Xor
    elif choiceBoolean == '3':
        image1_path = input("Masukkan Path Gambar 1: ")
        image2_path = input("Masukkan Path Gambar 2: ")
        booleanXor.boolean_xor(image1_path, image2_path)
    
    else:
        print("Invalid choice. Please choose a valid option.")

def option_6():
    print("1.Translasi")
    print("2.Rotasi")
    print("3.Flipping")
    print("4.Zooming")

    choiceGeometri = input("Masukan No Pilihan Operasi : ")

    #Translasi
    if choiceGeometri == '1':
        image_path = input("Masukkan Path Gambar: ")
    # Input validation for Slide_Horizontal
        while True:
            Slide_Horizontal = input("Masukkan Jarak Geser Horizontal (X) : ")
            try:
                Slide_Horizontal = int(Slide_Horizontal)
                break  # Exit the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for Slide_Horizontal.")

        # Input validation for Slide_Vertical
        while True:
            Slide_Vertical = input("Masukkan Jarak Geser Vertical (Y) : ")
            try:
                Slide_Vertical = int(Slide_Vertical)
                break  # Exit the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for Slide_Vertical.")

        Translation.perform_translation(image_path,Slide_Horizontal,Slide_Vertical)

    #Rotasi
    elif choiceGeometri == '2':
        image_path = input("Masukkan Path Gambar: ")
    # Input validation for Slide_Horizontal
        while True:
            AngleRotate = input("Masukkan Derajat Rotasi : ")
            try:
                AngleRotate = int(AngleRotate)
                break  # Exit the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for Slide_Horizontal.")

        Rotation.perform_rotation(image_path,AngleRotate)

    #Flipping    
    elif choiceGeometri == '3':
        image_path = input("Masukkan Path Gambar: ")
    # Input validation for Slide_Horizontal
        while True:
            TypeFlip = input("Masukkan Type Flip 0 = Horizontal, 1 = Vertikal  ")
            try:
                TypeFlip = int(TypeFlip)
                break  # Exit the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for Slide_Horizontal.")

        Flip.perform_flip(image_path,TypeFlip)

    #Zooming    
    elif choiceGeometri == '4':
        image_path = input("Masukkan Path Gambar: ")
    # Input validation for Slide_Horizontal
        while True:
            ZoomParameter = input("Masukkan Berapa Kali Zoom : ")
            try:
                ZoomParameter = int(ZoomParameter)
                break  # Exit the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for Slide_Horizontal.")

        Zooming.perform_zoom(image_path,ZoomParameter)
    else:
        print("Invalid choice. Please choose a valid option.")

    

def main():
    while True:
        print("\nMenu:")
        print("1. Citra Negatif")
        print("2. Citra GrayScale")
        print("3. Image Brightening")
        print("4. Operasi Aritmatika 2 Buah Citra")
        print("5. Option Boolean Pada Citra")
        print("6. Operasi Geometri")
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
