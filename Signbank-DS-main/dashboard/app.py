import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SignBank AI - EDA Dashboard",
    layout="wide"
)

# =====================================================
# CLASS NAMES
# =====================================================

CLASS_NAMES = [
    "0","1","10","100","1000",
    "2","20","3","4","5",
    "50","500","6","7","8","9",
    "A","ATM","B","C","D","E",
    "G","H","I","J","JUTA",
    "K","Kartu ATM","L","M",
    "MILYAR","N","O","P","Q",
    "R","RIBU","S","Saldo",
    "T","Transfer","U","Uang",
    "V","W","X","Y","Z"
]

# =====================================================
# PATH
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset_final"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_dataset():

    X_train = np.load(
        os.path.join(
            DATASET_DIR,
            "X_train.npy"
        )
    )

    X_val = np.load(
        os.path.join(
            DATASET_DIR,
            "X_val.npy"
        )
    )

    X_test = np.load(
        os.path.join(
            DATASET_DIR,
            "X_test.npy"
        )
    )

    y_train = np.load(
        os.path.join(
            DATASET_DIR,
            "y_train.npy"
        )
    )

    y_val = np.load(
        os.path.join(
            DATASET_DIR,
            "y_val.npy"
        )
    )

    y_test = np.load(
        os.path.join(
            DATASET_DIR,
            "y_test.npy"
        )
    )

    return (
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test
    )

(
    X_train,
    X_val,
    X_test,
    y_train,
    y_val,
    y_test
) = load_dataset()

# =====================================================
# HEADER
# =====================================================

st.title("🤟 SignBank AI")
st.subheader(
    "Exploratory Data Analysis Dashboard"
)

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.header("Project Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Classes",
    49
)

col2.metric(
    "Total Samples",
    5094
)

col3.metric(
    "Sequence Length",
    40
)

col4.metric(
    "Features",
    141
)

st.write("---")

# =====================================================
# DATASET OVERVIEW
# =====================================================

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Train Samples",
    len(X_train)
)

col2.metric(
    "Validation Samples",
    len(X_val)
)

col3.metric(
    "Test Samples",
    len(X_test)
)

# =====================================================
# INPUT SHAPE
# =====================================================

st.header("Input Shape")

shape_df = pd.DataFrame({
    "Property": [
        "Sequence Length",
        "Feature Count"
    ],
    "Value": [
        X_train.shape[1],
        X_train.shape[2]
    ]
})

st.dataframe(
    shape_df,
    use_container_width=True
)

# =====================================================
# DATASET SPLIT
# =====================================================

st.header("Dataset Split")

split_df = pd.DataFrame({
    "Dataset": [
        "Train",
        "Validation",
        "Test"
    ],
    "Samples": [
        len(X_train),
        len(X_val),
        len(X_test)
    ]
})

fig_split = px.pie(
    split_df,
    names="Dataset",
    values="Samples",
    title="Dataset Split Distribution"
)

st.plotly_chart(
    fig_split,
    use_container_width=True
)

# =====================================================
# CLASS DISTRIBUTION
# =====================================================

st.header("Class Distribution")

all_labels = np.concatenate([
    y_train,
    y_val,
    y_test
])

label_counts = (
    pd.Series(all_labels)
    .value_counts()
    .sort_index()
)

dist_df = pd.DataFrame({
    "Label": [
        CLASS_NAMES[i]
        for i in label_counts.index
    ],
    "Count": label_counts.values
})

fig_class = px.bar(
    dist_df,
    x="Label",
    y="Count",
    title="Sample Distribution per Class"
)

st.plotly_chart(
    fig_class,
    use_container_width=True
)

# =====================================================
# FEATURE DISTRIBUTION
# =====================================================

st.header("Feature Distribution")

sample_feature = X_train.reshape(
    -1,
    X_train.shape[-1]
)

feature_index = st.slider(
    "Select Feature Index",
    0,
    140,
    0
)

fig_feature = px.histogram(
    sample_feature[:, feature_index],
    nbins=50,
    title=f"Feature Distribution #{feature_index}"
)

st.plotly_chart(
    fig_feature,
    use_container_width=True
)

# =====================================================
# ANGLE FEATURE ANALYSIS
# =====================================================

st.header("Angle Feature Analysis")

angle_idx = st.selectbox(
    "Select Angle Feature",
    list(range(126, 141))
)

fig_angle = px.histogram(
    sample_feature[:, angle_idx],
    nbins=50,
    title=f"Angle Feature #{angle_idx}"
)

st.plotly_chart(
    fig_angle,
    use_container_width=True
)

# =====================================================
# SAMPLE SEQUENCE VISUALIZATION
# =====================================================

st.header("Sample Sequence Visualization")

sample_idx = st.slider(
    "Select Sample",
    0,
    len(X_train) - 1,
    0
)

feature_seq = st.slider(
    "Select Sequence Feature",
    0,
    140,
    0,
    key="sequence_feature"
)

seq_df = pd.DataFrame({
    "Frame": np.arange(
        X_train.shape[1]
    ),
    "Value": X_train[
        sample_idx,
        :,
        feature_seq
    ]
})

fig_seq = px.line(
    seq_df,
    x="Frame",
    y="Value",
    title=f"Feature {feature_seq} Across 40 Frames"
)

st.plotly_chart(
    fig_seq,
    use_container_width=True
)

# =====================================================
# BUSINESS QUESTIONS & CONCLUSIONS
# =====================================================

st.header("Business Questions & Conclusions")

st.markdown("""
### 1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Berdasarkan hasil Data Gathering, Data Cleaning, Dataset Validation, dan Feature Engineering, dataset berhasil dipersiapkan dengan kualitas yang baik untuk proses pelatihan model. Dataset terdiri dari **5.094 video gesture valid**, **49 kelas**, dan distribusi data yang relatif seimbang dengan **imbalance ratio sebesar 1,54**.

Setiap video direpresentasikan menjadi sequence berukuran **(40, 141)** yang terdiri dari **126 fitur landmark tangan** dan **15 fitur sudut (angle feature)**. Representasi ini mampu menangkap informasi posisi dan bentuk tangan yang dibutuhkan untuk proses klasifikasi gesture.

Hasil EDA menunjukkan bahwa dataset telah memenuhi kebutuhan dasar untuk membangun model klasifikasi gesture yang diharapkan mampu mencapai tingkat akurasi tinggi pada tahap pelatihan dan evaluasi.

---

### 2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Dataset yang digunakan mencakup alfabet, angka, istilah perbankan, dan istilah keuangan yang umum digunakan dalam interaksi layanan perbankan.

Selain itu, data dikumpulkan dari **6 kontributor berbeda** dengan variasi:

- Latar belakang
- Pencahayaan
- Sudut pengambilan video
- Variasi gerakan tangan

Keberagaman data tersebut meningkatkan peluang model untuk mengenali gesture secara lebih robust pada kondisi nyata sehingga dapat mendukung komunikasi antara nasabah Tuli dan petugas bank secara lebih efektif.

Meskipun performa akhir sistem masih harus dibuktikan melalui tahap pelatihan dan evaluasi model, kualitas dataset yang telah tervalidasi memberikan fondasi yang kuat untuk pengembangan sistem penerjemah bahasa isyarat perbankan.

---

### Kesimpulan EDA

- Total Sampel: 5.094 video
- Total Kelas: 49 gesture
- Total Kontributor: 6 orang
- Sequence Length: 40 frame
- Total Feature: 141 fitur
- Dataset Status: VALID
- Success Rate Landmark Extraction: 100%

Seluruh tahapan Data Science sebelum modeling telah berhasil diselesaikan. Dataset akhir siap digunakan untuk proses pelatihan model LSTM guna mengembangkan sistem penerjemah bahasa isyarat perbankan yang mendukung komunikasi yang lebih inklusif bagi nasabah Tuli.

---

### Catatan Jumlah Kelas

Pada tahap perencanaan awal, dataset dirancang terdiri dari **50 kelas gesture**.

Namun hasil validasi menunjukkan bahwa dataset akhir terdiri dari **49 kelas**. Setelah dilakukan pemeriksaan terhadap seluruh label yang tersedia, ditemukan bahwa gesture huruf **"F"** tidak terdapat pada dataset akhir sehingga tidak ikut diproses pada tahap feature engineering dan dataset preparation.

Akibatnya jumlah kelas yang digunakan dalam penelitian menjadi **49 kelas**, namun seluruh kelas yang tersedia memiliki jumlah sampel yang memadai dengan minimum **100 sampel per kelas** sehingga dataset tetap layak digunakan untuk pelatihan model.
""")

# =====================================================
# DATASET SAMPLE
# =====================================================

st.header("Dataset Sample")

st.write(
    "Sample Shape:",
    X_train[sample_idx].shape
)

sample_df = pd.DataFrame(
    X_train[sample_idx]
)

st.dataframe(
    sample_df.head(10),
    use_container_width=True
)

# =====================================================
# FOOTER
# =====================================================

st.write("---")

st.caption(
    "SignBank AI | Exploratory Data Analysis Dashboard"
)
