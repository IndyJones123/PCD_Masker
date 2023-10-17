import cv2 #cv2 untuk pengolahan gambar dan video
import numpy as np #numpy untuk operasi numerik
from mtcnn import MTCNN #MTCNN untuk deteksi wajah
from keras.models import load_model # load_model dan image dari Keras untuk memuat model dan memproses gambar
from keras.preprocessing import image

# Load model yang telah dilatih
model = load_model('best.h5')  # Gantilah dengan jalur ke model yang telah Anda simpan

# Menginisialisasi detektor wajah menggunakan MTCNN.
detector = MTCNN()

# Mendefinisikan fungsi detect_faces dengan parameter frame, yang bertugas mendeteksi wajah pada suatu frame.
def detect_faces(frame): #Menggunakan detektor wajah (MTCNN) untuk mendeteksi wajah dalam frame.
    results = detector.detect_faces(frame)

    for result in results: #Melakukan iterasi pada hasil deteksi wajah.
        x, y, w, h = result['box'] 
        confidence = result['confidence'] #Mengambil koordinat dan dimensi kotak wajah (x, y, w, h) serta tingkat kepercayaan deteksi (confidence).

        # Memeriksa apakah tingkat kepercayaan deteksi melebihi 0.1.
        if confidence > 0.1:  
            # Gambar kotak wajah
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Crop wajah
            face = frame[y:y + h, x:x + w] #Jika ya, menggambar kotak di sekitar wajah dan memotong area wajah dari frame.

            # Ubah ukuran wajah sesuai dengan model
            img = cv2.resize(face, (224, 224)) #Mengubah ukuran wajah sesuai dengan ukuran yang diperlukan oleh model (224x224).
            img = image.img_to_array(img) #Mengkonversi gambar wajah ke array dan melakukan normalisasi dengan membagi setiap piksel dengan 255.0.
            img = img / 255.0  # Normalisasi gambar

            prediction = model.predict(np.expand_dims(img, axis=0)) #Melakukan prediksi klasifikasi (masker atau tidak masker) menggunakan model yang telah dimuat (model.predict).
            if prediction[0][0] > prediction[0][1]: #Menentukan label berdasarkan hasil prediksi.
                label = "Bermasker"
            else:
                label = "Tidak Bermasker"

            # Menampilkan label hasil prediksi di atas kotak wajah dengan menggunakan cv2.putText.
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Fungsi untuk melakukan prediksi dari webcam
def predict_webcam():
    cap = cv2.VideoCapture(0)  # Membuka kamera menggunakan cv2.VideoCapture. 
    cap.set(3, 640)  # Mengatur Lebar frame
    cap.set(4, 480)  # Mengatur Tinggi frame
    cap.set(5, 60)  # Mengatur frame rate menjadi 15 FPS


    while True: #Memulai loop tak terbatas untuk membaca frame dari kamera.
        ret, frame = cap.read() 

        frame_with_faces = detect_faces(frame) #Memanggil fungsi detect_faces untuk mendeteksi dan melakukan prediksi pada wajah.

        cv2.imshow('Webcam', frame_with_faces)  #Menampilkan hasil prediksi secara real-time pada video dari webcam.

        if cv2.waitKey(1) & 0xFF == ord('q'):  #Memberhentikan tampilan video saat tombol 'q' ditekan.
            break

    cap.release()
    cv2.destroyAllWindows()

# Contoh penggunaan
# predict_webcam()
