import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="FutureColor Bot - Computer Expo",
    page_icon="🎉",
    layout="centered"
)

# -------------------------------------------------------
# -------------------- CUSTOM CSS -----------------------
# -------------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe9d6, #fff4e3, #fbe4c2);
    background-size: cover;
}

/* Clean Header Box */
.header-clean {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 25px;
    backdrop-filter: blur(8px);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.28);
}

/* Title text */
.header-title {
    font-size: 42px;
    font-weight: 900;
    color: #A020F0;
    margin-bottom: 8px;
}

/* Subheading */
.header-sub {
    font-size: 28px;
    font-weight: 700;
    color: #FF1493;
    margin-top: -10px;
}

/* Footer small text */
.header-small {
    font-size: 18px;
    font-weight: 500;
    color: #fff;
    opacity: 0.9;
}

/* Logo */
.logo-img {
    width: 130px;
    margin-bottom: 10px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# -------------------- HEADER SECTION -------------------
# -------------------------------------------------------

AMRITA_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Amrita_Vishwa_Vidyapeetham_Logo.png/800px-Amrita_Vishwa_Vidyapeetham_Logo.png"

st.markdown(f"""
<div class="header-clean">
    <img src="{AMRITA_LOGO}" class="logo-img">
    <div class="header-title">Welcome to the Computer Expo 2025 🎉</div>
    <div class="header-sub">Amrita Vidyalayam</div>
    <div class="header-small">A Creative Project by Grade 7 Students 💻✨</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# -------------------- CSV STORAGE ----------------------
# -------------------------------------------------------

CSV_FILE = "futurecolor_data.csv"

# Create file first time
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df_init.to_csv(CSV_FILE, index=False)

# -------------------------------------------------------
# ----------------------- FORM --------------------------
# -------------------------------------------------------

name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox(
    "🎨 Your Favourite Color",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
)

# -------------------------------------------------------
# ---------------- FUTURE MESSAGES ----------------------
# -------------------------------------------------------

messages = {
    "Red": (
        "🔥 You are bold, passionate, and full of unstoppable energy!\n\n"
        "Your future is filled with exciting adventures and leadership opportunities.\n\n"
        "People naturally look up to you because of your confidence and strong personality.\n\n"
        "A bright and thrilling path awaits you!"
    ),

    "Blue": (
        "🌊 Calm, intelligent, and thoughtful — you bring peace wherever you go.\n\n"
        "You will achieve great success in academics and creative thinking.\n\n"
        "A future filled with knowledge and meaningful achievements is waiting for you!"
    ),

    "Green": (
        "🌿 You have a gentle heart and a peaceful soul.\n\n"
        "Your kindness and creativity will inspire many people.\n\n"
        "A beautiful, harmonious journey lies ahead for you!"
    ),

    "Yellow": (
        "🌟 Cheerful, bright, and full of brilliant ideas — you are a natural creator!\n\n"
        "You will shine in everything you do, especially in creativity and teamwork!"
    ),

    "Purple": (
        "🔮 Unique, imaginative, and thoughtful.\n\n"
        "Your innovative ideas will one day make a real difference in the world!"
    ),

    "Pink": (
        "💖 Loving, joyful, and kind.\n\n"
        "Your future is filled with happiness and positive relationships!"
    ),

    "Black": (
        "⚫ Strong, focused, and determined.\n\n"
        "Your discipline and resilience guarantee huge success ahead!"
    ),

    "White": (
        "🤍 Calm, pure, and peaceful.\n\n"
        "You bring harmony wherever you go — a beautiful journey awaits!"
    )
}

# -------------------------------------------------------
# ------------------ SUBMIT BUTTON ----------------------
# -------------------------------------------------------

if st.button("✨ Reveal My Future"):
    if name == "" or city == "":
        st.error("Please fill all fields!")
    else:
        msg = messages[color]

        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to CSV (cloud safe)
        df = pd.read_csv(CSV_FILE)
        new_row = {
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        st.success("🎉 Your response has been saved securely!")

# -------------------------------------------------------
# ------------------- ADMIN PANEL -----------------------
# -------------------------------------------------------

st.write("---")
st.header("🔒 Admin Access Only")

ADMIN_PASSWORD = "amrita123"

admin_pw = st.text_input("Enter admin password:", type="password")

if st.button("🔐 Login"):
    if admin_pw == ADMIN_PASSWORD:
        st.success("Admin access granted ✔")

        df_show = pd.read_csv(CSV_FILE)
        st.dataframe(df_show)

        # Download CSV
        with open(CSV_FILE, "rb") as f:
            st.download_button("📥 Download CSV File", f, file_name="futurecolor_data.csv")
    else:
        st.error("❌ Incorrect password")

# -------------------------------------------------------
# --------------------- FOOTER --------------------------
# -------------------------------------------------------

st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
