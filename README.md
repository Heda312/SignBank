# SignBank AI - Exploratory Data Analysis Dashboard

## Deskripsi Proyek

SignBank AI merupakan sistem penerjemah bahasa isyarat perbankan berbasis Artificial Intelligence yang dikembangkan untuk membantu komunikasi antara nasabah Tuli dan petugas bank.

Dashboard ini digunakan untuk menampilkan hasil Exploratory Data Analysis (EDA) terhadap dataset bahasa isyarat perbankan yang telah melalui proses Data Gathering, Data Cleaning, Dataset Validation, Feature Engineering, dan Dataset Preparation.

---

## Dataset Information

| Komponen        | Nilai     |
| --------------- | --------- |
| Total Samples   | 5094      |
| Total Classes   | 49        |
| Contributors    | 6 Orang   |
| Resolution      | 512 × 512 |
| FPS             | 30        |
| Duration        | 2–5 Detik |
| Sequence Length | 40        |
| Total Features  | 141       |
| Dataset Type    | Primer    |

---

## Feature Information

Setiap video diekstraksi menggunakan MediaPipe Hands dan direpresentasikan sebagai:

(40, 141)

Keterangan:

| Feature Type         | Total |
| -------------------- | ----- |
| Landmark Coordinates | 126   |
| Angle Features       | 15    |
| Total Features       | 141   |

---

## Struktur Folder

SignBank_Cloud/
│
├── app/
│   └── app.py
│
├── dataset_final/
│   ├── X_train.npy
│   ├── X_val.npy
│   ├── X_test.npy
│   ├── y_train.npy
│   ├── y_val.npy
│   └── y_test.npy
│
├── docs/
├── reports/
├── src/
│
├── requirements.txt
└── README.md

---

## Dashboard Features

Dashboard menyediakan visualisasi:

* Dataset Overview
* Project Statistics
* Dataset Split Distribution
* Class Distribution
* Feature Distribution
* Angle Feature Analysis
* Sample Sequence Visualization
* Business Questions Analysis
* EDA Conclusions
* Dataset Sample Preview

---

## Business Questions

### 1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Pertanyaan ini digunakan untuk mengukur kemampuan model dalam mengenali gesture bahasa isyarat perbankan menggunakan metrik Accuracy, Precision, Recall, dan F1-Score.

### 2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Pertanyaan ini digunakan untuk mengevaluasi sejauh mana hasil prediksi model dapat digunakan sebagai media komunikasi pada konteks layanan perbankan.

---

## Instalasi

Clone repository:

git clone <repository-url>
cd SignBank_Cloud

Install dependency:

pip install -r requirements.txt

---

## Menjalankan Dashboard Streamlit

Dari root project:

streamlit run app/app.py

atau

python -m streamlit run app/app.py

Setelah berhasil dijalankan, dashboard dapat diakses melalui browser:

http://localhost:8501

---

## Requirements

Contoh isi requirements.txt:

streamlit
plotly
numpy
pandas

---

## Kesimpulan Dataset

Dataset akhir berhasil dipersiapkan untuk tahap pemodelan dengan karakteristik:

* 5094 sampel gesture valid
* 49 kelas bahasa isyarat
* Distribusi data relatif seimbang
* Success rate landmark extraction 100%
* Representasi data berbentuk sequence (40,141)

Dataset siap digunakan untuk proses pelatihan model Long Short-Term Memory (LSTM) guna mengembangkan sistem penerjemah bahasa isyarat perbankan secara real-time.

---

## Catatan

Pada tahap perencanaan awal, dataset dirancang terdiri dari 50 kelas gesture. Namun setelah proses validasi ditemukan bahwa gesture huruf "F" tidak tersedia pada dataset akhir sehingga jumlah kelas yang digunakan menjadi 49 kelas.

Meskipun demikian, seluruh kelas yang tersedia memiliki jumlah sampel yang memadai dan layak digunakan untuk proses pelatihan model.