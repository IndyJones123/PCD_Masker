import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def perform_normalisasi(image):
    print(image)
    # Check if the image is not None
    if image is not None:

        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Compute the histogram of the grayscale image before normalization
        hist_original = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])

        # Manually normalize the grayscale image
        min_pixel_value = np.min(grayscale_image)
        max_pixel_value = np.max(grayscale_image)
        normalized_image = ((grayscale_image - min_pixel_value) / (max_pixel_value - min_pixel_value) * 255).astype(np.uint8)

        # Compute the histogram of the normalized grayscale image
        hist_normalized = cv2.calcHist([normalized_image], [0], None, [256], [0, 256])

        # Display the normalized image
        cv2.imshow("Before Normalized Image", grayscale_image)

        # Display the normalized image
        cv2.imshow("After Normalized Image", normalized_image)

        # Create a single plot to display both histograms
        plt.figure(figsize=(12, 6))
        
        # Plot the histogram of the grayscale image before normalization (in blue)
        plt.subplot(1, 2, 1)
        plt.title("Histogram of Grayscale Image (Before Normalization)")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.plot(hist_original, color='blue')
        plt.xlim([0, 256])

        # Plot the histogram of the normalized grayscale image (in red)
        plt.subplot(1, 2, 2)
        plt.title("Histogram of Grayscale Image (After Normalization)")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.plot(hist_normalized, color='red')
        plt.xlim([0, 256])

        plt.tight_layout()
        plt.show()

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to load the image.")

# # Create a tkinter window to open the file dialog
# root = tk.Tk()
# root.withdraw()  # Hide the main tkinter window

# # Ask the user to select an image file using the file dialog
# file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])

# # Read the selected image file
# selected_image = cv2.imread(file_path)

# # Call the function with the selected image
# perform_normalisasi(selected_image)
