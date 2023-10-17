import cv2
import numpy as np 
from mtcnn import MTCNN
from keras.models import load_model
from keras.preprocessing import image

# Load model yang telah dilatih
model = load_model('best3.h5')  # Gantilah dengan jalur ke model yang telah Anda simpan

# Inisialisasi detektor wajah (MTCNN)
detector = MTCNN()

# Fungsi untuk mendeteksi wajah dalam setiap frame video
def detect_faces(frame):
    results = detector.detect_faces(frame)

    for result in results:
        x, y, w, h = result['box']
        confidence = result['confidence']

        # Filter deteksi dengan tingkat kepercayaan tertentu
        if confidence > 0.1:
            # Gambar kotak wajah
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Crop wajah
            face = frame[y:y + h, x:x + w]

            # Ubah ukuran wajah sesuai dengan model
            img = cv2.resize(face, (224, 224))
            img = image.img_to_array(img)
            img = img / 255.0  # Normalisasi gambar

            prediction = model.predict(np.expand_dims(img, axis=0))
            if prediction[0][0] > prediction[0][1]:
                label = "Bermasker"
            else:
                label = "Tidak Bermasker"

            # Tampilkan label di atas kotak wajah
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Fungsi untuk melakukan prediksi dari webcam
def predict_webcam():
    cap = cv2.VideoCapture(0)  # 0 untuk kamera utama, atau ganti dengan 1 untuk kamera lain jika ada
    cap.set(3, 640)  # Lebar frame
    cap.set(4, 480)  # Tinggi frame
    cap.set(5, 60)  # Atur frame rate menjadi 15 FPS


    while True:
        ret, frame = cap.read()

        frame_with_faces = detect_faces(frame)

        cv2.imshow('Webcam', frame_with_faces)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Contoh penggunaan
# predict_webcam()
