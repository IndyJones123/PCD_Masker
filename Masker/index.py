import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import predictionImage
import predictionVideoCam
import predictionVideo
import tempfile
import os

# Functions that take an image parameter
def function1(image, file_path):
    # Save the image to a temporary file
    temp_image_path = os.path.join(tempfile.gettempdir(), 'temp_image.png')
    image.save(temp_image_path)

    # Replace this with your logic for function 1
    predictionImage.predict_and_show_image(temp_image_path)

def function2():
    # Replace this with your logic for function 2
    predictionVideoCam.predict_webcam()

def function3():
    # Replace this with your logic for function 3
    video_file = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov")])
    if video_file:
        videoname = os.path.basename(video_file)
        output_video_name = videoname.rsplit('.', 1)[0] + "_output.mp4"
        predictionVideo.predict_and_save_video(video_file, output_video_name )

# Function to open a file dialog for image selection
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image

        image_label.photo = photo  # Store a reference to prevent garbage collection
        image_label.pack()
        
        function1(image, file_path)

# Create the main window
root = tk.Tk()
root.title("MaskerDetectionApp")

# Create an image label
image_label = tk.Label(root)
image_label.pack()

# Create a frame to contain buttons with flexible row layout
button_frame = tk.Frame(root)
button_frame.pack()

# Load and display the logo image
logo_image = Image.open("logo.jpeg")  # Replace with your logo file
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack()

# Create buttons to execute functions
button2 = tk.Button(button_frame, text="Prediksi Klasifikasi Masker (VideoCam)", command=lambda: function2())
# Create buttons to execute functions
button3 = tk.Button(button_frame, text="Prediksi Klasifikasi Masker (Video)", command=lambda: function3())
# Create a button to open the file dialog
open_button = tk.Button(button_frame, text="Prediksi Klasifikasi Masker (Gambar)", command=open_image)
button2.config(pady=5)  # Add 5 pixels padding above and below the text
open_button.config(pady=5)
button3.config(pady=5)


# Pack the buttons and logo
button2.pack(side=tk.LEFT, padx=5)
open_button.pack(side=tk.LEFT, padx=5)
button3.pack(side=tk.LEFT, padx=5)

root.mainloop()
