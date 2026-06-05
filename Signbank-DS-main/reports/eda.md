# Exploratory Data Analysis (EDA)

## Tujuan EDA

Exploratory Data Analysis (EDA) dilakukan untuk memahami karakteristik dataset, mengevaluasi distribusi data, mengidentifikasi potensi permasalahan pada dataset, serta memperoleh insight yang dapat mendukung pengembangan model SignBank AI.

EDA dilakukan menggunakan dataset hasil Data Cleaning, Dataset Validation, dan Feature Engineering yang telah dipersiapkan untuk proses pelatihan model.

---

# Dataset Overview

Dataset SignBank AI merupakan dataset primer yang dikumpulkan secara mandiri untuk mendukung pengembangan sistem penerjemah bahasa isyarat perbankan.

| Informasi      | Nilai     |
| -------------- | --------- |
| Total Sampel   | 5094      |
| Total Kelas    | 49        |
| Kontributor    | 6 Orang   |
| Resolusi Video | 512 × 512 |
| FPS            | 30        |
| Durasi Video   | 2–5 Detik |
| Jenis Dataset  | Primer    |

Dataset terdiri dari gesture alfabet, angka, istilah perbankan, dan istilah keuangan yang umum digunakan pada layanan perbankan.

---

# Analisis Distribusi Dataset

Dataset dibagi menjadi tiga subset:

* Training Set
* Validation Set
* Test Set

Pembagian dataset dilakukan untuk memastikan model dapat dilatih, divalidasi, dan diuji menggunakan data yang berbeda sehingga menghasilkan evaluasi yang lebih objektif.

Insight:

* Dataset telah dipisahkan untuk menghindari overfitting.
* Setiap subset memiliki representasi seluruh kelas gesture.

---

# Analisis Distribusi Kelas

Hasil validasi menunjukkan:

| Metrik                | Nilai |
| --------------------- | ----- |
| Total Kelas           | 49    |
| Minimum Sampel/Kelas  | 100   |
| Maksimum Sampel/Kelas | 154   |
| Imbalance Ratio       | 1.54  |

Insight:

* Dataset memiliki distribusi yang relatif seimbang.
* Tidak ditemukan class imbalance yang signifikan.
* Seluruh kelas memiliki jumlah sampel yang cukup untuk proses pelatihan model.

---

# Analisis Feature Engineering

Feature Engineering dilakukan menggunakan MediaPipe Hands.

Setiap frame menghasilkan:

| Feature         | Jumlah |
| --------------- | ------ |
| Landmark Tangan | 126    |
| Angle Feature   | 15     |
| Total Feature   | 141    |

Representasi akhir setiap video:

(40, 141)

Keterangan:

* 40 frame sequence
* 141 fitur per frame

Insight:

* Landmark menangkap posisi tangan.
* Angle feature menangkap bentuk dan orientasi jari.
* Kombinasi kedua fitur diharapkan meningkatkan kemampuan model dalam membedakan gesture yang memiliki bentuk serupa.

---

# Analisis Sequence

Video memiliki durasi yang bervariasi antara 2–5 detik.

Untuk menyeragamkan ukuran input model, seluruh video dinormalisasi menjadi:

40 frame

Insight:

* Seluruh sampel memiliki ukuran input yang konsisten.
* Memudahkan proses pelatihan model LSTM.
* Mengurangi variasi panjang sequence antar video.

---

# Analisis Kualitas Dataset

Hasil Dataset Validation menunjukkan:

| Metrik                      | Nilai |
| --------------------------- | ----- |
| Dataset Status              | VALID |
| Success Landmark Extraction | 100%  |
| Failed Files                | 0     |

Insight:

* Dataset siap digunakan untuk proses pemodelan.
* Tidak ditemukan kegagalan ekstraksi fitur.
* Seluruh sampel berhasil diproses menjadi format numerik.

---

# Jawaban Pertanyaan Bisnis

## 1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Berdasarkan hasil EDA, dataset memiliki kualitas yang baik dengan distribusi kelas yang relatif seimbang serta representasi fitur yang informatif. Kondisi ini memberikan fondasi yang kuat untuk menghasilkan model dengan performa yang baik pada tahap pelatihan dan evaluasi.

## 2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Dataset mencakup berbagai istilah yang relevan dengan layanan perbankan dan dikumpulkan dari berbagai kondisi lingkungan. Hal ini diharapkan mampu meningkatkan kemampuan model dalam mengenali gesture pada kondisi penggunaan nyata sehingga dapat mendukung komunikasi yang lebih inklusif.

---

# Kesimpulan EDA

Hasil EDA menunjukkan bahwa dataset SignBank AI memiliki kualitas yang baik, distribusi yang relatif seimbang, serta representasi fitur yang sesuai untuk digunakan pada model Long Short-Term Memory (LSTM).

Dataset siap digunakan pada tahap pelatihan dan evaluasi model untuk menjawab pertanyaan bisnis yang telah ditentukan.