# Import library yang dibutuhkan
from sklearn.metrics import confusion_matrix, classification_report 
import numpy as np
import tensorflow as tf #pengembangan model jaringan saraf tiruan 
from keras.applications import VGG16
from keras.models import Model
from keras.layers import Flatten, Dense
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator #untuk proses melakukan preprocessing image
from keras.utils import to_categorical

# Buat generator untuk data training
train_data_dir = './Dataset/training' #berisi path direktori tempat data training disimpan
test_data_dir = './Dataset/testing' #berisi path direktori tempat data testing disimpan
img_height, img_width = 224, 224 #persamaan ukuran tinggi dan lebar gambar dari seluruh data
batch_size = 32 #jumlah sampel data yang digunakan pada setiap iterasi

train_datagen = ImageDataGenerator(
    rescale=1./255, #preprocessing untuk mengubah skala piksel gambar
    shear_range=0.2, #mengontrol sejauh 0,2 gambar dapat diputar
    zoom_range=0.2, #Seluruh gambar diperbesar sebanyak 0,2
    horizontal_flip=True) #pemutaran gambar secara horizontal

train_generator = train_datagen.flow_from_directory( #memproses data training yang akan digunakan untuk melatih model
    train_data_dir, #memuat gambar dari direktori data training untuk diproses selama pelatihan model
    target_size=(img_height, img_width), #target dari gambar-gambar yang telah diprocessing disesuaikan dengan penentuan lebar dan tinggi gambar yang telah didefinisikan
    batch_size=batch_size, #model akan mengikuti jumlah sampel data yang akan digunakan pada setiap iterasi
    class_mode='categorical') #mengatur cara label kelas diproses dan dihasilkan dengan kelas categorial karena terdiri dari 2 class

# Membangun arsitektur model
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))
x = base_model.output
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# Freeze layer-layer VGG16
for layer in base_model.layers:
    layer.trainable = False

# Compile model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Melatih model
model.fit(train_generator, epochs=5)

# Simpan model
model.save('best3.h5')

# Uji model
test_datagen = ImageDataGenerator(rescale=1./255) #Menginisialisasi objek untuk memproses data uji, dengan mengubah skala nilai piksel ke rentang 0-1.
test_generator = test_datagen.flow_from_directory(  #Membuat generator data uji dari sebuah direktori, dengan spesifikasi target ukuran gambar, batch size, mode kelas, dan pengacakan tertentu.
    test_data_dir,
    target_size=(img_height, img_width),
    batch_size=1,
    class_mode='categorical',
    shuffle=False)


# Prediksi kelas data uji
predictions = model.predict(test_generator) #Melakukan prediksi kelas data uji menggunakan model yang telah di-train sebelumnya.
predicted_classes = np.argmax(predictions, axis=1) #Mengambil kelas yang diprediksi dari hasil probabilitas prediksi.

# Dapatkan ground truth (kelas sebenarnya) dari generator
true_classes = test_generator.classes

# Hitung confusion matrix
confusion = confusion_matrix(true_classes, predicted_classes) #Menghitung confusion matrix untuk mengevaluasi performa model.
print("Confusion Matrix:") #mencetak judul dari confusion matrix
print(confusion) #Mencetak isi dari confusion matrix.

# Cetak laporan klasifikasi
class_labels = list(test_generator.class_indices.keys()) #Mendapatkan label kelas dari generator data uji.
report = classification_report(true_classes, predicted_classes, target_names=class_labels) #Menghasilkan laporan evaluasi model.
print("Classification Report:") #Mencetak judul "Classification Report".
print(report) #Mencetak laporan evaluasi model yang mencakup berbagai metrik, lalu kita akan execute file index.py

# Evaluasi model
evaluation = model.evaluate(test_generator) #Menggunakan metode evaluate pada model untuk mengevaluasi performa model menggunakan data uji (test_generator).
print("Akurasi:", evaluation[1] * 100, "%") #Mencetak akurasi evaluasi model dalam persentase.
