import Translation;
import Rotation;


def option_1():
    print("Option 1 selected.")
      
def option_2():
    print("Option 2 selected. You can put your code here.")

def option_3():
    print("Option 3 selected. You can put your code here.")

def option_4():
    print("Option 4 selected. You can put your code here.")

def option_5():
    print("Option 4 selected. You can put your code here.")

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
        option_3()

    #Zooming    
    elif choiceGeometri == '4':
        option_4()
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

