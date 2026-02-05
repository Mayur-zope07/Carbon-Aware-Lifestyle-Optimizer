# ============================================================
# Carbon-Aware Lifestyle Optimizer — Streamlit App
# ============================================================

# ─── IMPORTS ───────────────────────────────────────────────
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from backend.auth import login, signup
from backend.calculator import calculate_total
from backend.recommender import carbon_level, generate_recommendations
from backend.database import create_tables, cursor, conn





# ─── PAGE CONFIG ───────────────────────────────────────────
st.set_page_config(
    page_title="Carbon-Aware Lifestyle Optimizer",
    layout="wide"
)
# ─── SIMPLE ENCODERS FOR ML INPUT ──────────────────────────
VEHICLE_MAP = {
    "Car": 0,
    "Bus": 1,
    "Truck": 2,
    "Motorcycle": 3
}

FUEL_MAP = {
    "Petrol": 0,
    "Diesel": 1,
    "Electric": 2,
    "Hybrid": 3
}


# ─── LOAD ML MODEL ─────────────────────────────────────────
model = joblib.load("emission_model.pkl")

# ─── DATABASE INIT ─────────────────────────────────────────
create_tables()

# ─── SESSION STATE ─────────────────────────────────────────
if "user" not in st.session_state:
    st.session_state.user = None


# ============================================================
# 🔐 LOGIN / SIGNUP
# ============================================================
if st.session_state.user is None:
    st.title("🔐 Login / Signup")

    choice = st.radio("Choose an option", ["Login", "Signup"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button(choice):
        if choice == "Signup":
            if signup(username, password):
                st.success("Account created. Please login.")
            else:
                st.error("Username already exists.")
        else:
            user = login(username, password)
            if user:
                st.session_state.user = user[0]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()


# ============================================================
# 🌱 MAIN APP
# ============================================================

st.sidebar.success("🌱 Logged in")

if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()

st.markdown("""
<style>
body { background-color: #f0fff4; }
h1, h2, h3 { color: #2f855a; }
.stButton > button {
    background-color: #38a169;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 Carbon-Aware Lifestyle Optimizer")
st.subheader("Green Skills • Sustainable Living • AI Powered")
st.markdown("---")


# ============================================================
# 📑 TABS
# ============================================================
tab1, tab2 = st.tabs(["🌍 Lifestyle Calculator", "🤖 ML Vehicle Prediction"])


# ============================================================
# 🌍 TAB 1 — LIFESTYLE CALCULATOR
# ============================================================
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        vehicle_type = st.selectbox(
            "Select your vehicle",
            ["bike", "petrol_car", "diesel_car", "ev", "bus", "train"]
        )
        vehicle_km = st.slider("Daily travel (km)", 0, 100, 10)
        electricity_kwh = st.slider("Daily electricity usage (kWh)", 0, 20, 5)

    with col2:
        food_type = st.selectbox("Food habit", ["veg", "mixed", "non_veg"])
        waste_kg = st.slider("Daily waste generated (kg)", 0.0, 5.0, 1.0)

    st.markdown("---")

    if st.button("🌍 Calculate My Carbon Impact"):
        inputs = {
            "vehicle_type": vehicle_type,
            "vehicle_km": vehicle_km,
            "electricity_kwh": electricity_kwh,
            "food_type": food_type,
            "waste_kg": waste_kg
        }

        result = calculate_total(inputs)
        level = carbon_level(result["total"])

        # Save prediction
        cursor.execute(
            """
            INSERT INTO predictions (user_id, vehicle_type, total_co2, level)
            VALUES (?, ?, ?, ?)
            """,
            (st.session_state.user, vehicle_type, result["total"], level)
        )
        conn.commit()

        # Metrics
        st.success(f"🌿 Total CO₂ Emission: **{result['total']} kg/day**")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("🚗 Vehicle", f"{result['vehicle']} kg")
        m2.metric("⚡ Electricity", f"{result['electricity']} kg")
        m3.metric("🍽 Food", f"{result['food']} kg")
        m4.metric("♻️ Waste", f"{result['waste']} kg")

        # Charts
        df_chart = pd.DataFrame({
            "Source": ["Vehicle", "Electricity", "Food", "Waste"],
            "CO2 (kg)": [
                result["vehicle"],
                result["electricity"],
                result["food"],
                result["waste"]
            ]
        })

        c1, c2 = st.columns(2)

        with c1:
            st.plotly_chart(
                px.pie(
                    df_chart,
                    names="Source",
                    values="CO2 (kg)",
                    title="🌍 Carbon Emission Breakdown",
                    color_discrete_sequence=px.colors.sequential.Greens
                ),
                use_container_width=True
            )

        with c2:
            st.plotly_chart(
                px.bar(
                    df_chart,
                    x="Source",
                    y="CO2 (kg)",
                    title="📊 Emission by Category",
                    color="Source",
                    color_discrete_sequence=px.colors.sequential.Greens
                ),
                use_container_width=True
            )

        st.subheader("🤖 AI Recommendations")
        st.info(f"🌍 Carbon Impact Level: **{level}**")
        for tip in generate_recommendations(result, inputs):
            st.write(tip)


# ============================================================
# 🤖 TAB 2 — ML PREDICTION
# ============================================================
with tab2:
    st.subheader("🤖 ML-Based Vehicle Emission Prediction")

    vehicle_ml = st.selectbox("Vehicle Type", ["Car", "Bus", "Truck", "Motorcycle"])
    fuel_ml = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])
    engine_ml = st.number_input("Engine Size (L)", 0.5, 10.0, 1.5)
    age_ml = st.number_input("Vehicle Age (years)", 0, 30, 5)
    mileage_ml = st.number_input("Mileage (km)", 0, 30000, 10000)


    if st.button("Predict Emission Level"):

     st.write("Model expects:", model.feature_names_in_)

    input_data = {}

    for feature in model.feature_names_in_:
        input_data[feature] = 0

    if "Vehicle Type" in input_data:
        input_data["Vehicle Type"] = VEHICLE_MAP.get(vehicle_ml, 0)

    if "Fuel Type" in input_data:
        input_data["Fuel Type"] = FUEL_MAP.get(fuel_ml, 0)

    if "Engine Size" in input_data:
        input_data["Engine Size"] = engine_ml

    if "Age of Vehicle" in input_data:
        input_data["Age of Vehicle"] = age_ml

    if "Mileage" in input_data:
        input_data["Mileage"] = mileage_ml

    input_df = pd.DataFrame([input_data])[model.feature_names_in_]

    prediction = model.predict(input_df)[0]

    st.success(f"🚦 Predicted Emission Level: **{prediction}**")


# ============================================================
# 📜 HISTORY + 📈 TRENDS + CSV EXPORT
# ============================================================
st.markdown("---")
st.subheader("📜 Your Past Predictions")

cursor.execute(
    """
    SELECT timestamp, total_co2, level
    FROM predictions
    WHERE user_id = ?
    ORDER BY timestamp
    """,
    (st.session_state.user,)
)

rows = cursor.fetchall()

if rows:
    trend_df = pd.DataFrame(rows, columns=["Date", "Total CO₂", "Level"])
    trend_df["Date"] = pd.to_datetime(trend_df["Date"])

    st.dataframe(trend_df, use_container_width=True)

    # CSV Export
    st.download_button(
        "⬇️ Download History (CSV)",
        trend_df.to_csv(index=False),
        "carbon_history.csv",
        "text/csv"
    )

    # Trend chart
    st.plotly_chart(
        px.line(
            trend_df,
            x="Date",
            y="Total CO₂",
            markers=True,
            title="📈 Carbon Emission Trend",
            color_discrete_sequence=px.colors.sequential.Greens
        ),
        use_container_width=True
    )
else:
    st.info("No history available yet.")


# ============================================================
# 🏆 LEADERBOARD
# ============================================================
st.markdown("---")
st.subheader("🏆 Community Carbon Leaderboard (Anonymous)")

cursor.execute("""
    SELECT u.username, AVG(p.total_co2) AS avg_co2
    FROM predictions p
    JOIN users u ON p.user_id = u.id
    GROUP BY u.username
    ORDER BY avg_co2 ASC
    LIMIT 10
""")

lb = cursor.fetchall()

if lb:
    lb_df = pd.DataFrame(lb, columns=["User", "Avg CO₂ (kg/day)"])
    st.dataframe(lb_df, use_container_width=True)
else:
    st.info("Not enough data for leaderboard yet.")
