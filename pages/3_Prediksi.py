import streamlit as st
import pandas as pd
import joblib

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon="🩺",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def kategori_umur(umur):

    if umur <= 24:
        return 1
    elif umur <= 29:
        return 2
    elif umur <= 34:
        return 3
    elif umur <= 39:
        return 4
    elif umur <= 44:
        return 5
    elif umur <= 49:
        return 6
    elif umur <= 54:
        return 7
    elif umur <= 59:
        return 8
    elif umur <= 64:
        return 9
    elif umur <= 69:
        return 10
    elif umur <= 74:
        return 11
    elif umur <= 79:
        return 12
    else:
        return 13
    
education_map = {

    "Tidak Sekolah":1,

    "SD":2,

    "SMP":3,

    "SMA":4,

    "Diploma":5,

    "Sarjana":6

}

income_map = {

    "< Rp2 juta":1,

    "Rp2 - 5 juta":2,

    "Rp5 - 8 juta":3,

    "Rp8 - 11 juta":4,

    "Rp11 - 15 juta":5,

    "Rp15 - 20 juta":6,

    "Rp20 - 25 juta":7,

    "> Rp25 juta":8

}

def pilihan_ya_tidak(label):
    pilihan = st.radio(
        label,
        ["Ya", "Tidak"],
        horizontal=True
    )

    if pilihan == "Ya":
        return 1
    else:
        return 0

# ==========================================
# JUDUL
# ==========================================

st.title("🩺 Prediksi Risiko Diabetes")

st.markdown("""
Silakan isi data diri dan kondisi kesehatan Anda.
Sistem akan memprediksi risiko diabetes berdasarkan data yang dimasukkan.
""")

st.divider()

# ==========================================
# DATA PRIBADI
# ==========================================

st.header("👤 Data Pribadi")

col1, col2 = st.columns(2)

with col1:

    Sex = st.selectbox(
        "Jenis Kelamin",
        ["Laki-laki", "Perempuan"]
    )

with col2:

    umur = st.number_input(
        "Umur (Tahun)",
        min_value=18,
        max_value=120,
        value=30,
        step=1
    )

    col3, col4 = st.columns(2)

with col3:

    pendidikan = st.selectbox(
        "Pendidikan Terakhir",
        [
            "Tidak Sekolah",
            "SD",
            "SMP",
            "SMA",
            "Diploma",
            "Sarjana"
        ]
    )

with col4:

    pendapatan = st.selectbox(
        "Pendapatan per Bulan",
        [
            "< Rp2 juta",
            "Rp2 - 5 juta",
            "Rp5 - 8 juta",
            "Rp8 - 11 juta",
            "Rp11 - 15 juta",
            "Rp15 - 20 juta",
            "Rp20 - 25 juta",
            "> Rp25 juta"
        ]
    )

# ==========================================
# KONVERSI KE FORMAT DATASET
# ==========================================

if Sex == "Laki-laki":
    Sex = 1
else:
    Sex = 0

Age = kategori_umur(umur)

Education = education_map[pendidikan]

Income = income_map[pendapatan]

# ==========================================
# DATA FISIK
# ==========================================

st.divider()

st.header("📏 Data Fisik")

col1, col2 = st.columns(2)

with col1:

    berat = st.number_input(
        "Berat Badan (kg)",
        min_value=20.0,
        max_value=250.0,
        value=60.0,
        step=0.5
    )

with col2:

    tinggi = st.number_input(
        "Tinggi Badan (cm)",
        min_value=100.0,
        max_value=250.0,
        value=165.0,
        step=0.5
    )

tinggi_meter = tinggi / 100

BMI = round(
    berat / (tinggi_meter ** 2),
    1
)

st.metric(
    "BMI Anda",
    BMI
)

if BMI < 18.5:

    st.warning("Kategori BMI : Berat Badan Kurang")

elif BMI < 25:

    st.success("Kategori BMI : Normal")

elif BMI < 30:

    st.warning("Kategori BMI : Kelebihan Berat Badan")

else:

    st.error("Kategori BMI : Obesitas")

# ==========================================
# RIWAYAT PENYAKIT
# ==========================================

st.divider()

st.header("❤️ Riwayat Penyakit")

HighBP = pilihan_ya_tidak(
    "Apakah Anda memiliki tekanan darah tinggi?"
)

HighChol = pilihan_ya_tidak(
    "Apakah Anda memiliki kolesterol tinggi?"
)

CholCheck = pilihan_ya_tidak(
    "Apakah Anda pernah memeriksa kadar kolesterol?"
)

Stroke = pilihan_ya_tidak(
    "Apakah Anda pernah mengalami stroke?"
)

HeartDiseaseorAttack = pilihan_ya_tidak(
    "Apakah Anda pernah mengalami penyakit jantung atau serangan jantung?"
)

# ==========================================
# GAYA HIDUP
# ==========================================

st.divider()

st.header("🥗 Gaya Hidup")

Smoker = pilihan_ya_tidak(
    "Apakah Anda seorang perokok?"
)

PhysActivity = pilihan_ya_tidak(
    "Apakah Anda rutin melakukan aktivitas fisik?"
)

Fruits = pilihan_ya_tidak(
    "Apakah Anda rutin mengonsumsi buah setiap hari?"
)

Veggies = pilihan_ya_tidak(
    "Apakah Anda rutin mengonsumsi sayur setiap hari?"
)

HvyAlcoholConsump = pilihan_ya_tidak(
    "Apakah Anda mengonsumsi alkohol secara berlebihan?"
)

# ==========================================
# KONDISI KESEHATAN
# ==========================================

st.divider()

st.header("🩺 Kondisi Kesehatan")

col1, col2 = st.columns(2)

with col1:

    AnyHealthcare = pilihan_ya_tidak(
        "Apakah Anda memiliki asuransi kesehatan?"
    )

    NoDocbcCost = pilihan_ya_tidak(
        "Apakah Anda pernah tidak berobat karena biaya?"
    )

    DiffWalk = pilihan_ya_tidak(
        "Apakah Anda mengalami kesulitan berjalan?"
    )

with col2:

    GenHlth = st.select_slider(
        "Bagaimana kondisi kesehatan Anda secara umum?",
        options=[1,2,3,4,5],
        value=3,
        format_func=lambda x: {
            1:"⭐⭐⭐⭐⭐ Sangat Baik",
            2:"⭐⭐⭐⭐ Baik",
            3:"⭐⭐⭐ Cukup",
            4:"⭐⭐ Kurang",
            5:"⭐ Buruk"
        }[x]
    )

    MentHlth = st.slider(
        "Berapa hari Anda mengalami gangguan kesehatan mental dalam 30 hari terakhir?",
        0,
        30,
        0
    )

    PhysHlth = st.slider(
        "Berapa hari Anda mengalami gangguan kesehatan fisik dalam 30 hari terakhir?",
        0,
        30,
        0
    )

    # ==========================================
# DATA YANG AKAN DIPREDIKSI
# ==========================================

st.divider()

input_data = pd.DataFrame({

    "HighBP":[HighBP],
    "HighChol":[HighChol],
    "CholCheck":[CholCheck],
    "BMI":[BMI],
    "Smoker":[Smoker],
    "Stroke":[Stroke],
    "HeartDiseaseorAttack":[HeartDiseaseorAttack],
    "PhysActivity":[PhysActivity],
    "Fruits":[Fruits],
    "Veggies":[Veggies],
    "HvyAlcoholConsump":[HvyAlcoholConsump],
    "AnyHealthcare":[AnyHealthcare],
    "NoDocbcCost":[NoDocbcCost],
    "GenHlth":[GenHlth],
    "MentHlth":[MentHlth],
    "PhysHlth":[PhysHlth],
    "DiffWalk":[DiffWalk],
    "Sex":[Sex],
    "Age":[Age],
    "Education":[Education],
    "Income":[Income]

})

st.subheader("📋 Ringkasan Data")

st.dataframe(
    input_data,
    use_container_width=True
)

# ==========================================
# NORMALISASI
# ==========================================

input_scaled = scaler.transform(input_data)

st.divider()

prediksi = st.button(
    "🔍 Prediksi Risiko Diabetes",
    use_container_width=True,
    type="primary"
)

if prediksi:

    hasil = model.predict(input_scaled)[0]
    probabilitas = model.predict_proba(input_scaled)[0]

    st.header("📊 Hasil Prediksi")

    if hasil == 0:
        st.success("✅ Risiko : Tidak Diabetes")

    elif hasil == 1:
        st.warning("⚠️ Risiko : Prediabetes")

    else:
        st.error("🚨 Risiko : Diabetes")

    # ==========================
    # GRAFIK
    # ==========================

    st.subheader("📈 Grafik Probabilitas")

    chart = pd.DataFrame({
        "Kategori": [
            "Tidak Diabetes",
            "Prediabetes",
            "Diabetes"
        ],
        "Probabilitas": [
            probabilitas[0],
            probabilitas[1],
            probabilitas[2]
        ]
    })

    st.bar_chart(
        chart,
        x="Kategori",
        y="Probabilitas"
    )

    # ==========================
    # REKOMENDASI
    # ==========================

    st.subheader("💡 Rekomendasi")

    if hasil == 0:

        st.success("""

✅ Pertahankan pola hidup sehat

• Konsumsi buah dan sayur

• Olahraga minimal 30 menit

• Kurangi gula

• Hindari rokok

• Rutin cek kesehatan

""")
        
    elif hasil == 1:

        st.warning("""

⚠️ Anda memiliki risiko Prediabetes

• Kurangi makanan manis

• Perbanyak aktivitas fisik

• Turunkan berat badan

• Periksa gula darah secara rutin

""")
        
    else:

        st.error("""

🚨 Risiko Diabetes cukup tinggi

• Segera konsultasi ke dokter

• Lakukan pemeriksaan gula darah

• Terapkan pola makan sehat

• Ikuti anjuran tenaga medis

""")

    # ==========================
    # DOWNLOAD
    # ==========================

    hasil_text = (
        "Tidak Diabetes"
        if hasil == 0
        else "Prediabetes"
        if hasil == 1
        else "Diabetes"
    )

    ringkasan = input_data.copy()

    ringkasan["Hasil Prediksi"] = hasil_text

    csv = ringkasan.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📄 Download Hasil Prediksi",
        csv,
        "hasil_prediksi.csv",
        "text/csv"
    )
