import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# Konfigurasi Halaman
# ==========================================
st.set_page_config(
    page_title="Visualisasi Data",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Visualisasi Dataset Diabetes")

st.markdown("""
Halaman ini menampilkan berbagai visualisasi dari dataset
**Diabetes Health Indicators BRFSS 2015**.
""")

# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("dataset/diabetes_012_health_indicators_BRFSS2015.csv")

df = load_data()

# ==========================================
# Distribusi Target Diabetes
# ==========================================

st.subheader("1️⃣ Distribusi Kelas Diabetes")

kelas = df["Diabetes_012"].value_counts().sort_index()

fig = px.pie(
    values=kelas.values,
    names=["Tidak Diabetes", "Prediabetes", "Diabetes"],
    hole=0.45,
    title="Distribusi Target Diabetes"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Distribusi BMI
# ==========================================

st.subheader("2️⃣ Distribusi BMI")

fig = px.histogram(
    df,
    x="BMI",
    nbins=40,
    title="Distribusi Body Mass Index (BMI)"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Distribusi Umur
# ==========================================

st.subheader("3️⃣ Distribusi Umur")

age = df["Age"].value_counts().sort_index()

fig = px.bar(
    x=age.index,
    y=age.values,
    labels={
        "x":"Kategori Umur",
        "y":"Jumlah"
    },
    title="Distribusi Umur"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Jenis Kelamin
# ==========================================

st.subheader("4️⃣ Distribusi Jenis Kelamin")

sex = df["Sex"].value_counts()

fig = px.pie(
    values=sex.values,
    names=["Laki-laki","Perempuan"],
    hole=0.5,
    title="Distribusi Jenis Kelamin"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Tekanan Darah Tinggi
# ==========================================

st.subheader("5️⃣ High Blood Pressure")

bp = df["HighBP"].value_counts()

fig = px.bar(
    x=["Tidak","Ya"],
    y=bp.values,
    labels={
        "x":"High Blood Pressure",
        "y":"Jumlah"
    },
    title="Distribusi High Blood Pressure"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Kolesterol Tinggi
# ==========================================

st.subheader("6️⃣ High Cholesterol")

chol = df["HighChol"].value_counts()

fig = px.bar(
    x=["Tidak","Ya"],
    y=chol.values,
    labels={
        "x":"High Cholesterol",
        "y":"Jumlah"
    },
    title="Distribusi High Cholesterol"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Aktivitas Fisik
# ==========================================

st.subheader("7️⃣ Aktivitas Fisik")

activity = df["PhysActivity"].value_counts()

fig = px.pie(
    values=activity.values,
    names=["Tidak Aktif","Aktif"],
    hole=0.45,
    title="Aktivitas Fisik"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Heatmap Korelasi
# ==========================================

st.subheader("8️⃣ Heatmap Korelasi")

corr = df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Korelasi Antar Variabel"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Scatter BMI vs Age
# ==========================================

st.subheader("9️⃣ BMI vs Umur")

fig = px.scatter(
    df.sample(3000, random_state=42),
    x="BMI",
    y="Age",
    color=df.sample(3000, random_state=42)["Diabetes_012"].astype(str),
    title="Hubungan BMI dan Umur",
    labels={
        "color":"Diabetes"
    }
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Boxplot BMI
# ==========================================

st.subheader("🔟 Boxplot BMI Berdasarkan Diabetes")

fig = px.box(
    df,
    x="Diabetes_012",
    y="BMI",
    color="Diabetes_012",
    title="Perbandingan BMI pada Setiap Kelas Diabetes"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Visualisasi berhasil ditampilkan.")