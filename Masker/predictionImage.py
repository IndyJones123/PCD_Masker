import cv2
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load model yang telah dilatih
model = load_model('best.h5')  # Gantilah dengan jalur ke model yang telah Anda simpan

# Fungsi untuk melakukan prediksi dan menampilkan hasil pada gambar
def predict_and_show_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalisasi gambar

    prediction = model.predict(img)
    if prediction[0][0] > prediction[0][1]:
        label = "Bermasker"
    else:
        label = "Tidak Bermasker"

    # Load gambar asli
    original_image = cv2.imread(image_path)

    # Tampilkan hasil prediksi pada gambar
    cv2.putText(original_image, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Tampilkan gambar yang sudah dimodifikasi
    cv2.imshow(label, original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Contoh penggunaan
image_path = 'Gambar1.jpg'  # Gantilah dengan jalur ke gambar yang ingin Anda prediksi
predict_and_show_image(image_path)
