import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Personality Crystal Ball - Computer Expo",
    page_icon="🔮",
    layout="centered"
)

# ---------------- ADMIN SETTINGS ----------------
ADMIN_PASSWORD = "owner123"   # Change this for security
DATA_FILE = "secure_data.csv"  # Hidden CSV file

# ---------------- SETUP STORAGE ----------------
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Choice", "Personality Message"])
    df.to_csv(DATA_FILE, index=False)

# ---------------- AMRITA LOGO ----------------
logo_url = "https://amrita.edu/wp-content/uploads/2022/01/amrita-vidyalayam-logo.png"

st.markdown(f"""
<div style='text-align:center;'>
    <img src="{logo_url}" width="180">
    <h1 style='color:#8A2BE2; font-weight:900;'>Welcome to the Computer Expo 2025 🎉</h1>
    <h3 style='color:#FF1493;'>Presented by Grade 7 Students • Amrita Vidyalayam</h3>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------- PERSONALITY OPTIONS ----------------
st.markdown("### 🔮 Choose one option and I will reveal your personality!")

options = {
    "Adventurer": "🌟 You are brave, energetic, and love exploring new things! Your future is filled with exciting challenges and victories.",
    "Thinker": "🧠 You are calm, logical, and love solving puzzles. You will succeed in science, research, and innovation!",
    "Artist": "🎨 Creative, expressive, and full of imagination! You will shine in art, design, and storytelling.",
    "Leader": "👑 Confident, strong, and inspiring — people follow your ideas. A successful leadership future awaits you!",
    "Helper": "💖 Kind, supportive, and caring — you make people feel safe and valued. Your future impacts many lives positively.",
    "Inventor": "⚙️ Curious and innovative — you love building things. You will create something amazing one day!",
}

choice_list = list(options.keys())

# ---------------- FORM INPUTS ----------------
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
selected_choice = st.selectbox("✨ Choose the one that feels like you", choice_list)

# ---------------- REVEAL PERSONALITY BUTTON ----------------
if st.button("🔍 Reveal My Personality"):
    if name.strip() == "" or city.strip() == "":
        st.error("Please fill all fields!")
    else:
        personality_msg = options[selected_choice]

        st.success(f"Hi **{name}**, here is your personality:")
        st.info(personality_msg)

        # SAVE ENTRY
        df = pd.read_csv(DATA_FILE)
        new_row = {
            "Name": name,
            "Age": age,
            "City": city,
            "Choice": selected_choice,
            "Personality Message": personality_msg
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)

        st.success("Your response was saved securely! 🔐")

st.write("---")

# ---------------- ADMIN PANEL ----------------
st.markdown("## 🔒 Admin Panel (Owner only)")

admin_pass = st.text_input("Enter admin password", type="password")

if st.button("Unlock Admin Panel"):
    if admin_pass == ADMIN_PASSWORD:
        st.success("Admin Panel Unlocked ✔")

        df = pd.read_csv(DATA_FILE)
        st.write("### 📁 Saved Visitor Data")
        st.dataframe(df)

        st.download_button(
            label="📥 Download Data as CSV",
            data=df.to_csv(index=False),
            file_name="expo_personality_data.csv",
            mime="text/csv"
        )
    else:
        st.error("❌ Wrong admin password!")

st.write("---")

st.caption("© 2025 • Personality Crystal Ball • Computer Expo • Amrita Vidyalayam")
