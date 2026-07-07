import streamlit as st

# ==========================================
# Konfigurasi Halaman
# ==========================================
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Sidebar
# ==========================================
st.sidebar.title("🩺 Diabetes Prediction")

st.sidebar.markdown("""
### Menu
- 🏠 Home
- 📄 Dataset
- 📊 Visualisasi
- 🤖 Prediksi
- ℹ Tentang
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Aplikasi ini digunakan untuk memprediksi risiko diabetes menggunakan Machine Learning."
)

# ==========================================
# Judul
# ==========================================
st.title("🩺 Diabetes Prediction Dashboard")

st.markdown("""
### Prediksi Risiko Diabetes Menggunakan Machine Learning

Dataset yang digunakan merupakan **BRFSS 2015 Diabetes Health Indicators**.
Aplikasi ini dibangun menggunakan **Python**, **Scikit-Learn**, dan **Streamlit**.
""")

st.divider()

# ==========================================
# Statistik
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Jumlah Data",
        value="253.680"
    )

with col2:
    st.metric(
        label="Jumlah Fitur",
        value="21"
    )

with col3:
    st.metric(
        label="Target",
        value="Diabetes_012"
    )

st.divider()

# ==========================================
# Informasi
# ==========================================

st.subheader("📌 Tentang Dataset")

st.write("""
Dataset **Behavioral Risk Factor Surveillance System (BRFSS) 2015**
berisi berbagai indikator kesehatan masyarakat yang digunakan
untuk memprediksi kemungkinan seseorang mengalami diabetes.

Target klasifikasi terdiri dari:

- **0 = Tidak Diabetes**
- **1 = Prediabetes**
- **2 = Diabetes**
""")

st.divider()

# ==========================================
# Fitur
# ==========================================

st.subheader("✨ Fitur Aplikasi")

fitur1, fitur2 = st.columns(2)

with fitur1:

    st.success("✔ Preview Dataset")

    st.success("✔ Visualisasi Data")

    st.success("✔ Prediksi Diabetes")

with fitur2:

    st.success("✔ Confusion Matrix")

    st.success("✔ Akurasi Model")

    st.success("✔ Probabilitas Prediksi")

st.divider()

# ==========================================
# Cara Menggunakan
# ==========================================

st.subheader("📖 Cara Menggunakan")

st.markdown("""
1. Pilih menu **Dataset** untuk melihat data.

2. Pilih menu **Visualisasi** untuk melihat grafik.

3. Masuk ke menu **Prediksi**.

4. Masukkan seluruh indikator kesehatan.

5. Klik tombol **Prediksi**.

6. Sistem akan menampilkan hasil prediksi beserta probabilitasnya.
""")

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "© 2026 | Diabetes Prediction Dashboard | Streamlit + Scikit-Learn"
)