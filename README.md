# 🌱 Carbon-Aware Lifestyle Optimizer

A **data-driven, AI-assisted web application** that helps users calculate, visualize, and reduce their **daily carbon footprint** based on lifestyle choices such as vehicle usage, electricity consumption, food habits, and waste generation.

This project is built using **Streamlit**, **Python**, and **real-world Kaggle datasets**, focusing on **Green Skills**, sustainability awareness, and explainable carbon emission analysis.

---

## 🚀 Features

- 🚗 **Vehicle-wise Carbon Emission Calculation**
  - Distance-based CO₂ estimation
  - Uses real Kaggle vehicle emission data

- ⚡ **Electricity Emission Calculation**
  - Based on grid emission factors

- 🍽 **Food Habit Impact**
  - Veg / Mixed / Non-Veg comparison

- ♻️ **Waste Emission Estimation**
  - Solid waste based CO₂ calculation

- 📊 **Interactive Dashboard**
  - Pie chart & bar chart using Plotly
  - Clear visual breakdown of emissions

- 🤖 **AI-Based Recommendations**
  - Carbon Impact Level: **Low / Medium / High**
  - Personalized eco-friendly suggestions

- 🔐 **Basic Login System**
  - Demo-level authentication

- 🎨 **Green-Themed UI**
  - Eco-friendly colors
  - Clean and modern layout

---

## 🧠 Project Motivation

Climate change and rising carbon emissions are global challenges.  
This project aims to **educate users** and **encourage sustainable habits** by providing:

- Transparent carbon calculations  
- Real-world datasets  
- Actionable AI-driven recommendations  

The project is designed as a **learning + showcase application** aligned with **Green Skills and AI/ML initiatives**.

---

## 🗂️ Project Structure

Carbon-Aware-Lifestyle-Optimizer/
│
├── app.py # Main Streamlit application
│
├── backend/
│ ├── init.py
│ ├── calculator.py # Carbon calculation logic
│ └── recommender.py # AI recommendations & carbon level
│
├── data/
│ ├── vehicle_catalog.csv # Cleaned vehicle emission dataset
│ └── emission_factors.csv # Activity-based emission factors
│
├── scripts/
│ └── data_cleaning.py # Dataset preprocessing scripts
│
├── requirements.txt
└── README.md


---

## 📊 Datasets Used

### 1️⃣ Vehicle Emission Dataset
- Source: **Kaggle – Vehicle CO₂ Emission Datasets**
- Contains vehicle type, fuel type, and CO₂ emissions
- Cleaned and normalized to **kg/km**
- Used for precise distance-based vehicle emission calculation

### 2️⃣ Carbon Emission Factors Dataset
- Source: **Kaggle – Carbon Footprint / Lifestyle Datasets**
- Used for:
  - Electricity emissions
  - Food habit emissions
  - Waste emissions

> Raw Kaggle datasets are **processed and cleaned** before being used in the application.

---

## 🧮 Carbon Emission Calculation Logic

### 🚗 Vehicle Emission


### ⚡ Electricity Emission


### 🍽 Food & ♻️ Waste Emission


### 🌍 Total Carbon Footprint


---

## 🤖 AI Recommendation System

- **Carbon Impact Levels**
  - Low 🌱 → Eco-friendly lifestyle
  - Medium ⚠️ → Needs improvement
  - High 🔥 → High carbon footprint

- **AI Recommendations**
  - Reduce vehicle usage
  - Switch to public transport / EV
  - Optimize electricity usage
  - Improve food and waste habits

---

## 🛠️ Tech Stack

- **Frontend / UI**: Streamlit
- **Backend**: Python
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Datasets**: Kaggle (processed)
- **Deployment**: Streamlit Cloud

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-link>
cd Carbon-Aware-Lifestyle-Optimizer
