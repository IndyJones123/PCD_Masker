import cv2
import numpy as np

def perform_translation(image_path, tx, ty):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is not None:
        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Create an empty canvas with the same size as the original image
        height, width, channels = image.shape
        translated_image = np.zeros((height, width, channels), dtype=np.uint8)

        # Iterate through each pixel and copy it to the translated position
        for y in range(height):
            for x in range(width):
                new_x = x + tx
                new_y = y + ty

                if 0 <= new_x < width and 0 <= new_y < height:
                    translated_image[new_y, new_x] = image[y, x]

        # Display the original and translated images
        cv2.imshow("Original Image", image)
        cv2.imshow("Hasil Operasi Translasi Image", translated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to load the image.")

# perform_translation("Gambar.jpg", 100, 20)
