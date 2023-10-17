import cv2
import numpy as np 
from mtcnn import MTCNN #untuk deteksi wajah dan fitur wajah
from keras.models import load_model
from keras.preprocessing import image

# Load model yang telah dilatih
model = load_model('best.h5')  # Gantilah dengan jalur ke model yang telah Anda simpan

# Inisialisasi detektor wajah (MTCNN)
detector = MTCNN()

# Fungsi untuk mendeteksi wajah dalam setiap frame video
def detect_faces(frame):
    results = detector.detect_faces(frame) #memanggil fungsi detect_faces yang kemudian disimpan melalui param frame

    for result in results:
        x, y, w, h = result['box'] #mengambil kotak box
        confidence = result['confidence'] #mengambil tingkat confidence

        # Filter deteksi dengan tingkat kepercayaan tertentu
        if confidence > 0.3:
            # Memindai kotak wajah menjadi kotak
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

            # Tampilkan label masker atau tidak bermasker di atas kotak wajah
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Fungsi untuk melakukan prediksi dari video dan menyimpan sebagai MP4
def predict_and_save_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path) #membuka video di path menggunakan cv2
    
    # Set frame rate and frame size
    cap.set(cv2.CAP_PROP_FPS, 15)  # Set the frame rate to 30 FPS (adjust as needed)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the frame width (adjust as needed)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the frame height (adjust as needed)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # menyimpan video 
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (640, 480))  # Adjust frame size and frame rate

    while cap.isOpened(): #loop untuk membaca setiap frame video
        ret, frame = cap.read() #membaca frame dari video

        if not ret:
            break

        frame_with_faces = detect_faces(frame) #memanggil fungsi detect_faces

        out.write(frame_with_faces)  # menulis frame yang telah diproses

        cv2.imshow('Processed Video', frame_with_faces) #membuka video yang telah berlabel

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Contoh penggunaan

