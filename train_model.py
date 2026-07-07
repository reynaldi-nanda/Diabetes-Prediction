import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ============================
# 1. Membaca Dataset
# ============================
print("Membaca dataset...")

df = pd.read_csv("dataset/diabetes_012_health_indicators_BRFSS2015.csv")

print(df.head())

# ============================
# 2. Memisahkan Fitur dan Target
# ============================

X = df.drop("Diabetes_012", axis=1)
y = df["Diabetes_012"]

print("\nJumlah Data :", len(df))
print("Jumlah Fitur :", X.shape[1])

# ============================
# 3. Split Data
# ============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nData Training :", len(X_train))
print("Data Testing :", len(X_test))

# ============================
# 4. Normalisasi Data
# ============================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ============================
# 5. Membuat Model
# ============================

print("\nTraining Model...")

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# ============================
# 6. Prediksi
# ============================

y_pred = model.predict(X_test)

# ============================
# 7. Evaluasi
# ============================

akurasi = accuracy_score(y_test, y_pred)

print("\n==============================")
print("HASIL EVALUASI")
print("==============================")

print(f"Akurasi : {akurasi*100:.2f}%")

print("\nClassification Report")

print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

# ============================
# 8. Simpan Model
# ============================

joblib.dump(model, "model.pkl"compress=3)
joblib.dump(scaler, "scaler.pkl")

print("\nModel berhasil disimpan.")

print("File model.pkl berhasil dibuat.")
print("File scaler.pkl berhasil dibuat.")
