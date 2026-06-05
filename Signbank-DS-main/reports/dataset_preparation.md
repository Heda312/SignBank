# Dataset Preparation

## Tujuan

Dataset Preparation dilakukan untuk menghasilkan dataset akhir yang siap digunakan pada proses pelatihan model machine learning.

Tahap ini dilakukan setelah proses Feature Engineering selesai dilakukan.

---

# Input Dataset

Dataset hasil Feature Engineering disimpan dalam folder:

dataset_landmarks/

Format setiap sampel:

(40, 141)

Keterangan:

* 40 frame sequence
* 141 fitur per frame

---

# Proses Dataset Preparation

Tahapan yang dilakukan:

1. Membaca seluruh file landmark hasil ekstraksi.
2. Melakukan pelabelan berdasarkan nama folder gesture.
3. Melakukan encoding label menggunakan LabelEncoder.
4. Menggabungkan seluruh sampel menjadi dataset numerik.
5. Membagi dataset menjadi:

   * Training Set
   * Validation Set
   * Test Set
6. Menyimpan dataset dalam format NumPy.

---

# Struktur Dataset Akhir

Dataset akhir disimpan pada:

dataset_final/

Berisi:

dataset_final/
├── X_train.npy
├── X_val.npy
├── X_test.npy
├── y_train.npy
├── y_val.npy
├── y_test.npy
└── label_encoder.pkl

---

# Bentuk Data

Feature Shape:

(40, 141)

Keterangan:

| Komponen        | Nilai |
| --------------- | ----- |
| Sequence Length | 40    |
| Feature Count   | 141   |

---

# Pembagian Dataset

Dataset dibagi menjadi:

| Subset     | Fungsi                            |
| ---------- | --------------------------------- |
| Train      | Melatih model                     |
| Validation | Memantau performa selama training |
| Test       | Evaluasi akhir model              |

Tujuan pembagian dataset adalah menghasilkan evaluasi model yang lebih objektif dan mengurangi risiko overfitting.

---

# Hasil Dataset Preparation

| Metrik          | Nilai |
| --------------- | ----- |
| Total Sampel    | 5094  |
| Total Kelas     | 49    |
| Sequence Length | 40    |
| Total Feature   | 141   |

Seluruh data berhasil dikonversi ke format numerik dan siap digunakan pada proses pelatihan model.

---

# Kesiapan Dataset untuk Modeling

Dataset akhir telah memenuhi kebutuhan pemodelan karena:

* Seluruh sampel memiliki ukuran yang seragam.
* Data telah direpresentasikan dalam bentuk numerik.
* Distribusi kelas relatif seimbang.
* Tidak ditemukan data rusak pada tahap validasi.
* Feature extraction berhasil dilakukan pada seluruh sampel.

---

# Kesimpulan

Tahap Dataset Preparation berhasil menghasilkan dataset akhir yang siap digunakan untuk proses pelatihan model Long Short-Term Memory (LSTM).

Dataset terdiri dari 5094 sampel, 49 kelas gesture, dan representasi fitur berukuran (40, 141) yang telah memenuhi kebutuhan untuk tahap modeling dan evaluasi.