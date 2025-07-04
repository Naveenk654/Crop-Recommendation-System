# 🌾 Crop Recommendation System

This is a simple but powerful ML-based project that helps suggest the best crop to grow based on your soil and weather data. It uses FastAPI for the backend and Streamlit for a clean user interface
---

## 🧠 Overview

### 🔍 Purpose
Help farmers and agricultural professionals make better crop-growing decisions by combining soil inputs with weather data from the user's city.

### 💡 Features

- 🧪 Accepts soil parameters (N, P, K, pH)
- 🌦️ Fetches real-time weather data using **Visual Crossing API**
- 🌱 Predicts the best crop using a trained ML model
- 📘 Also gives a short explanation on why a crop is suitable under your current conditions.
- ⚡ FastAPI backend + Streamlit frontend

---

## 📷 Screenshot

> ![image](https://github.com/user-attachments/assets/b0d8589f-c504-4cb3-9491-f9eee3f3343f)


---

## ⚙️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Backend     | Python, FastAPI, Uvicorn |
| Frontend    | Streamlit              |
| ML Model    | scikit-learn, pandas   |
| Weather API | Visual Crossing API    |

---

## 📥 Inputs

- **N** – Nitrogen level in soil
- **P** – Phosphorus level
- **K** – Potassium level
- **pH** – Acidity of the soil
- **City** – Location to fetch weather data (temperature, humidity, precipitation)

---

## 📤 Output

```json
{
  "predicted_crop": "maize",
  "why": "Maize grows well in well-drained soil with warm temperatures and moderate humidity — ideal for kharif or summer cropping."
}
## ▶️ How to Start This Project Locally

Make sure Python is installed (preferably Python 3.10+).

### 📌 Step 1: Clone the Repository

```bash
git clone https://github.com/Naveenk654/Crop-Recommendation-System.git
cd Crop-Recommendation-System
📌Step 2: Install Dependencies
pip install -r requirements.txt
📌 Step 3: Add Your Visual Crossing API Key
API_KEY = "YOUR_API_KEY"
📌 Step 4: Run the Backend
python -m uvicorn main:app --reload
📌 Step 5: Run the Frontend (Streamlit)
streamlit run app.py
## 🔮 Future Plan: Upload Soil Reports & Analyze Crop Benefits

### 📄 1. Upload Soil Report Documents
We plan to support uploading scanned or digital soil reports (PDF/images). The system will automatically extract:

- Nitrogen (N), Phosphorus (P), Potassium (K)
- pH levels

Using:
- OCR (Optical Character Recognition) for image-based reports
- PDF text parsing for digital reports

This will eliminate manual data entry and make the app easier for real-world usage by farmers and agronomists.

---

### 📈 2. Crop Benefits Analysis (Economic & Agronomic Insights)

In future updates, the system will provide a **detailed benefits analysis** for the recommended crop, including:

- 💰 **Estimated market price** and profit per acre
- 📈 **Market demand trend**
- 🔁 **Crop rotation compatibility**
- 💧 **Water use efficiency**
- 👨‍🌾 **Ease of cultivation and labor requirement**

This feature will help users not only grow the best crop but also make **informed economic decisions** based on data-driven insights.
🙌 Acknowledgements
This project was created as part of a learning journey combining machine learning, APIs, and full-stack development.
Open to feedback, ideas, and collaboration.

— Built by Naveen Kumawat
