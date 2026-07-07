import streamlit as st
import pandas as pd

# ==========================================
# Konfigurasi Halaman
# ==========================================
st.set_page_config(
    page_title="Dataset",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Dataset Diabetes BRFSS 2015")

st.markdown("""
Halaman ini menampilkan informasi lengkap mengenai dataset yang
digunakan untuk membangun model prediksi diabetes.
""")

# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/diabetes_012_health_indicators_BRFSS2015.csv")
    return df

df = load_data()

# ==========================================
# Statistik Dataset
# ==========================================

st.subheader("📊 Informasi Dataset")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Data", len(df))

with col2:
    st.metric("Jumlah Kolom", len(df.columns))

with col3:
    st.metric("Missing Value", int(df.isnull().sum().sum()))

st.divider()

# ==========================================
# Preview Dataset
# ==========================================

st.subheader("👀 Preview Dataset")

jumlah = st.slider(
    "Jumlah data yang ditampilkan",
    5,
    100,
    10
)

st.dataframe(
    df.head(jumlah),
    use_container_width=True
)

st.divider()

# ==========================================
# Nama Kolom
# ==========================================

st.subheader("📌 Daftar Kolom")

kolom = pd.DataFrame({
    "No": range(1, len(df.columns)+1),
    "Nama Kolom": df.columns
})

st.dataframe(
    kolom,
    use_container_width=True
)

st.divider()

# ==========================================
# Tipe Data
# ==========================================

st.subheader("🗂️ Tipe Data")

dtype = pd.DataFrame({
    "Kolom": df.columns,
    "Tipe Data": df.dtypes.astype(str)
})

st.dataframe(
    dtype,
    use_container_width=True
)

st.divider()

# ==========================================
# Statistik Deskriptif
# ==========================================

st.subheader("📈 Statistik Deskriptif")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# ==========================================
# Missing Value
# ==========================================

st.subheader("❗ Missing Value")

missing = pd.DataFrame({
    "Kolom": df.columns,
    "Jumlah Missing": df.isnull().sum(),
    "Persentase (%)": round(df.isnull().mean()*100,2)
})

st.dataframe(
    missing,
    use_container_width=True
)

st.divider()

# ==========================================
# Distribusi Target
# ==========================================

st.subheader("🎯 Distribusi Target")

target = df["Diabetes_012"].value_counts().sort_index()

st.bar_chart(target)

st.write(target)

st.info("""
Keterangan Target:

0 = Tidak Diabetes

1 = Prediabetes

2 = Diabetes
""")

st.divider()

# ==========================================
# Download Dataset
# ==========================================

st.subheader("⬇️ Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Dataset CSV",
    data=csv,
    file_name="diabetes_dataset.csv",
    mime="text/csv"
)

st.divider()

st.success("Dataset berhasil dimuat.")