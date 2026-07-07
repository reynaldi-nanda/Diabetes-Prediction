import streamlit as st
import pandas as pd
import joblib

# ==========================================
# Konfigurasi Halaman
# ==========================================
st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Prediksi Risiko Diabetes")

st.markdown("""
Masukkan data kondisi kesehatan Anda pada form di bawah ini,
kemudian klik tombol **Prediksi** untuk mengetahui risiko diabetes.
""")

# ==========================================
# Load Model dan Scaler
# ==========================================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# ==========================================
# Form Input
# ==========================================
col1, col2 = st.columns(2)

with col1:

    HighBP = st.selectbox(
        "Tekanan Darah Tinggi (HighBP)",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    HighChol = st.selectbox(
        "Kolesterol Tinggi (HighChol)",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    CholCheck = st.selectbox(
        "Pernah Cek Kolesterol",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    BMI = st.slider(
        "BMI",
        10,
        60,
        25
    )

    Smoker = st.selectbox(
        "Perokok",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    Stroke = st.selectbox(
        "Pernah Stroke",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    HeartDiseaseorAttack = st.selectbox(
        "Penyakit Jantung / Serangan Jantung",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    PhysActivity = st.selectbox(
        "Aktivitas Fisik",
        [0, 1],
        format_func=lambda x: "Aktif" if x == 1 else "Tidak Aktif"
    )

    Fruits = st.selectbox(
        "Konsumsi Buah",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    Veggies = st.selectbox(
        "Konsumsi Sayur",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

with col2:

    HvyAlcoholConsump = st.selectbox(
        "Konsumsi Alkohol Berlebihan",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    AnyHealthcare = st.selectbox(
        "Memiliki Asuransi Kesehatan",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    NoDocbcCost = st.selectbox(
        "Tidak Berobat Karena Biaya",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    GenHlth = st.slider(
        "Kesehatan Umum (1 = Sangat Baik, 5 = Sangat Buruk)",
        1,
        5,
        3
    )

    MentHlth = st.slider(
        "Hari Gangguan Mental (30 Hari Terakhir)",
        0,
        30,
        0
    )

    PhysHlth = st.slider(
        "Hari Gangguan Fisik (30 Hari Terakhir)",
        0,
        30,
        0
    )

    DiffWalk = st.selectbox(
        "Kesulitan Berjalan",
        [0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

    Sex = st.selectbox(
        "Jenis Kelamin",
        [0, 1],
        format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan"
    )

    Age = st.slider(
        "Kategori Umur",
        1,
        13,
        7
    )

    Education = st.slider(
        "Tingkat Pendidikan",
        1,
        6,
        4
    )

    Income = st.slider(
        "Tingkat Pendapatan",
        1,
        8,
        4
    )

st.divider()

# ==========================================
# Data Input
# ==========================================

input_data = pd.DataFrame({
    "HighBP": [HighBP],
    "HighChol": [HighChol],
    "CholCheck": [CholCheck],
    "BMI": [BMI],
    "Smoker": [Smoker],
    "Stroke": [Stroke],
    "HeartDiseaseorAttack": [HeartDiseaseorAttack],
    "PhysActivity": [PhysActivity],
    "Fruits": [Fruits],
    "Veggies": [Veggies],
    "HvyAlcoholConsump": [HvyAlcoholConsump],
    "AnyHealthcare": [AnyHealthcare],
    "NoDocbcCost": [NoDocbcCost],
    "GenHlth": [GenHlth],
    "MentHlth": [MentHlth],
    "PhysHlth": [PhysHlth],
    "DiffWalk": [DiffWalk],
    "Sex": [Sex],
    "Age": [Age],
    "Education": [Education],
    "Income": [Income]
})

st.subheader("📋 Data yang Akan Diprediksi")
st.dataframe(input_data, use_container_width=True)

# ==========================================
# Normalisasi Data
# ==========================================

input_scaled = scaler.transform(input_data)

# ==========================================
# Tombol Prediksi
# ==========================================

st.divider()

if st.button("🔍 Prediksi Diabetes", use_container_width=True):

    # Prediksi kelas
    hasil = model.predict(input_scaled)[0]

    # Probabilitas
    probabilitas = model.predict_proba(input_scaled)[0]

    st.subheader("📊 Hasil Prediksi")

    # ============================
    # Tidak Diabetes
    # ============================
    if hasil == 0:

        st.success("✅ Hasil Prediksi : TIDAK DIABETES")

        st.metric(
            "Probabilitas",
            f"{probabilitas[0]*100:.2f}%"
        )

        st.balloons()

        st.info("""
### Rekomendasi

- Pertahankan pola makan sehat.
- Rutin berolahraga minimal 30 menit per hari.
- Perbanyak konsumsi buah dan sayur.
- Hindari merokok.
- Batasi konsumsi gula berlebih.
- Lakukan pemeriksaan kesehatan secara berkala.
        """)

    # ============================
    # Prediabetes
    # ============================
    elif hasil == 1:

        st.warning("⚠️ Hasil Prediksi : PREDIABETES")

        st.metric(
            "Probabilitas",
            f"{probabilitas[1]*100:.2f}%"
        )

        st.warning("""
### Rekomendasi

- Kurangi makanan tinggi gula.
- Kurangi minuman manis.
- Turunkan berat badan apabila berlebih.
- Olahraga minimal 150 menit per minggu.
- Rutin cek kadar gula darah.
- Konsultasikan dengan dokter jika diperlukan.
        """)

    # ============================
    # Diabetes
    # ============================
    else:

        st.error("🚨 Hasil Prediksi : DIABETES")

        st.metric(
            "Probabilitas",
            f"{probabilitas[2]*100:.2f}%"
        )

        st.error("""
### Rekomendasi

- Segera lakukan pemeriksaan ke dokter.
- Kontrol kadar gula darah secara rutin.
- Terapkan pola makan sehat.
- Hindari makanan tinggi gula dan lemak.
- Tingkatkan aktivitas fisik sesuai anjuran dokter.
- Minum obat sesuai resep apabila telah didiagnosis.
        """)

    st.divider()

    # ==========================================
    # Detail Probabilitas
    # ==========================================

    st.subheader("📈 Probabilitas Setiap Kelas")

    hasil_prob = {
        "Tidak Diabetes": probabilitas[0],
        "Prediabetes": probabilitas[1],
        "Diabetes": probabilitas[2]
    }

    st.bar_chart(hasil_prob)

    # ==========================================
    # Detail Nilai Probabilitas
    # ==========================================

    st.write("### Detail Nilai")

    st.write(
        f"🟢 Tidak Diabetes : **{probabilitas[0]*100:.2f}%**"
    )

    st.write(
        f"🟡 Prediabetes : **{probabilitas[1]*100:.2f}%**"
    )

    st.write(
        f"🔴 Diabetes : **{probabilitas[2]*100:.2f}%**"
    )

    st.divider()

    # ==========================================
    # Riwayat Prediksi
    # ==========================================

    st.subheader("📋 Ringkasan Data")

    hasil_text = (
        "Tidak Diabetes" if hasil == 0
        else "Prediabetes" if hasil == 1
        else "Diabetes"
    )

    ringkasan = input_data.copy()
    ringkasan["Hasil Prediksi"] = hasil_text

    st.dataframe(
        ringkasan,
        use_container_width=True
    )

    # ==========================================
    # Download Hasil
    # ==========================================

    csv = ringkasan.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Hasil Prediksi",
        data=csv,
        file_name="hasil_prediksi_diabetes.csv",
        mime="text/csv"
    )