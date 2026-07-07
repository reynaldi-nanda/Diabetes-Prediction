import streamlit as st

# ==========================================
# Konfigurasi Halaman
# ==========================================
st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="ℹ️",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("ℹ️ Tentang Aplikasi")

st.markdown("""
Aplikasi ini dibuat sebagai implementasi **Machine Learning**
untuk memprediksi risiko diabetes berdasarkan indikator kesehatan.
""")

st.divider()

# ==========================================
# Informasi Aplikasi
# ==========================================

st.subheader("📌 Informasi Aplikasi")

col1, col2 = st.columns(2)

with col1:

    st.info("""
**Nama Aplikasi**

Diabetes Prediction Dashboard
""")

    st.info("""
**Versi**

1.0
""")

    st.info("""
**Bahasa Pemrograman**

Python
""")

with col2:

    st.info("""
**Framework**

Streamlit
""")

    st.info("""
**Machine Learning**

Scikit-Learn
""")

    st.info("""
**Model**

Random Forest Classifier
""")

st.divider()

# ==========================================
# Dataset
# ==========================================

st.subheader("📊 Dataset")

st.write("""
Dataset yang digunakan adalah:

**Diabetes Health Indicators BRFSS 2015**

Dataset ini berasal dari
Behavioral Risk Factor Surveillance System (BRFSS)
yang dikelola oleh Centers for Disease Control and Prevention (CDC).

Dataset memiliki:

- 253.680 data
- 22 kolom
- 21 fitur
- 1 target (Diabetes_012)

Target:

0 = Tidak Diabetes

1 = Prediabetes

2 = Diabetes
""")

st.divider()

# ==========================================
# Algoritma
# ==========================================

st.subheader("🤖 Algoritma")

st.success("""
Model yang digunakan adalah:

✔ Random Forest Classifier

Keunggulan:

✔ Akurasi tinggi

✔ Cocok untuk klasifikasi

✔ Tidak mudah overfitting

✔ Dapat menangani data dalam jumlah besar
""")

st.divider()

# ==========================================
# Teknologi
# ==========================================

st.subheader("💻 Teknologi")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Python", "3.x")

with col2:
    st.metric("Streamlit", "Latest")

with col3:
    st.metric("Scikit-Learn", "Latest")

st.divider()

# ==========================================
# Cara Kerja
# ==========================================

st.subheader("⚙ Cara Kerja Sistem")

st.markdown("""
1. Pengguna memasukkan data kesehatan.

2. Data dinormalisasi menggunakan StandardScaler.

3. Data diproses oleh model Random Forest.

4. Model melakukan klasifikasi.

5. Sistem menampilkan:

- Hasil Prediksi
- Probabilitas
- Rekomendasi
""")

st.divider()

# ==========================================
# Fitur Aplikasi
# ==========================================

st.subheader("✨ Fitur Aplikasi")

st.success("✔ Dashboard")

st.success("✔ Preview Dataset")

st.success("✔ Statistik Dataset")

st.success("✔ Visualisasi Data")

st.success("✔ Prediksi Diabetes")

st.success("✔ Probabilitas Prediksi")

st.success("✔ Download Hasil Prediksi")

st.divider()

# ==========================================
# Pengembang
# ==========================================

st.subheader("👨‍💻 Pengembang")

st.write("""
Nama : **Ervi**

Program Studi : **Informatika**

Universitas : **Universitas Respati Yogyakarta**

Mata Kuliah : **Data Science for Health**

Tahun : **2026**
""")

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "© 2026 Diabetes Prediction Dashboard | Dibangun menggunakan Streamlit dan Scikit-Learn"
)