import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import NormalisasiHistogram

# Functions that take an image parameter
def function1(image):
    # Replace this with your logic for function 1
    NormalisasiHistogram.perform_normalisasi(image)

def function2(image):
    # Replace this with your logic for function 2
    pass

def function3(image):
    # Replace this with your logic for function 3
    pass

# Function to open a file dialog for image selection
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    
    
    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300), Image.Resampling.NEAREST)  # Resize the image for display
        image = ImageTk.PhotoImage(image=image)
        image_label.config(image=image)
        image_label.image = image  # Keep a reference to avoid garbage collection
        image_label.matrix = cv2.imread(file_path)
        # Enable the function buttons
        button1.config(state=tk.NORMAL)
        button2.config(state=tk.NORMAL)
        button3.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Histogram App")

# Create an image label
image_label = tk.Label(root)
image_label.pack()

# Create buttons to execute functions
button1 = tk.Button(root, text="Normalisasi Histogram", command=lambda: function1(image_label.matrix))
button2 = tk.Button(root, text="Equalization Histogram", command=lambda: function2(image_label.matrix))
button3 = tk.Button(root, text="Stretching Histogram", command=lambda: function3(image_label.matrix))

# Initially, disable the function buttons until an image is selected
button1.config(state=tk.DISABLED)
button2.config(state=tk.DISABLED)
button3.config(state=tk.DISABLED)

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Pack the buttons
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
