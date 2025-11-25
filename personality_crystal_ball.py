import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Future Personality Bot",
    page_icon="🔮",
    layout="centered"
)

# ---------------- ADMIN SETTINGS ----------------
ADMIN_PASSWORD = "owner123"   # <-- CHANGE THIS TO ANY PASSWORD YOU WANT
DATA_FILE = "secure_data.csv"  # Hidden CSV file

# ---------------- INITIAL SETUP ----------------
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favourite Color", "Message"])
    df.to_csv(DATA_FILE, index=False)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center; color:#8A2BE2;'>🔮 Future Predictor 2025</h1>
<h3 style='text-align:center; color:#FF1493;'>Amrita Vidyalayam • Computer Expo</h3>
""", unsafe_allow_html=True)

st.write("### Tell me about you and I will reveal your colourful future! 🎨✨")

# ---------------- USER FORM ----------------
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")

color = st.selectbox(
    "🎨 Choose Your Favourite Color",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
)

# ---------------- FUTURE MESSAGES ----------------
messages = {
    "Red": "🔥 You are bold, passionate, and full of unstoppable energy! Leaders like you shape the future.",
    "Blue": "🌊 Calm and intelligent — your future is filled with academic success and deep wisdom.",
    "Green": "🌿 Kind-hearted and peaceful — you inspire everyone around you.",
    "Yellow": "🌟 Bright and cheerful — your creativity will take you far!",
    "Purple": "🔮 Unique thinker — your imagination will change the world!",
    "Pink": "💖 Loving and joyful — friendships and happiness follow you.",
    "Black": "⚫ Strong and determined — success is guaranteed in your journey.",
    "White": "🤍 Pure and calm — you spread peace wherever you go."
}

# ---------------- REVEAL BUTTON ----------------
if st.button("✨ Reveal My Future"):
    if name.strip() == "" or city.strip() == "":
        st.error("Please fill all fields properly!")
    else:
        future_msg = messages[color]
        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(future_msg)

        # Save Data
        df = pd.read_csv(DATA_FILE)
        new_row = {
            "Name": name,
            "Age": age,
            "City": city,
            "Favourite Color": color,
            "Message": future_msg
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)

        st.success("Your response has been saved securely! 🔐")

st.write("---")

# ---------------- ADMIN PANEL ----------------
st.markdown("## 🔒 Admin Panel (Owner Only)")

admin_input = st.text_input("Enter admin password to view data", type="password")

if st.button("Unlock Admin Panel"):
    if admin_input == ADMIN_PASSWORD:
        st.success("Admin Panel Unlocked ✔")

        df = pd.read_csv(DATA_FILE)
        st.write("### 📁 Visitor Data")
        st.dataframe(df)

        st.download_button(
            label="📥 Download Data as CSV",
            data=df.to_csv(index=False),
            file_name="visitor_data.csv",
            mime="text/csv"
        )

    else:
        st.error("❌ Wrong admin password!")


# ---------------- FOOTER ----------------
st.write("---")
st.caption("© 2025 • Future Predictor Bot • Made with ❤️ for Computer Expo")
