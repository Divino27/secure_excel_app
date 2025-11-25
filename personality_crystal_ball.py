import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="FutureColor Bot - Computer Expo",
    page_icon="🎉",
    layout="centered"
)

CSV_FILE = "futurecolor_cloud.csv"
ADMIN_PASSWORD = "amrita123@"   # <-- change if you want

# ---------------- CREATE CSV IF NOT EXISTS ----------------
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_csv(CSV_FILE, index=False)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe9d6, #fff4e3, #fbe4c2);
    background-size: cover;
}

/* HEADER BOX */
.header-box {
    background: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.20);
    margin-bottom: 25px;
}

/* Logo */
.header-logo {
    width: 180px;
    border-radius: 20px;
    margin-bottom: 10px;
}

/* Robot */
.header-robot {
    width: 120px;
    margin-top: -5px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #9b5cff, #d633ff);
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 18px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
# ---------------- HEADER SECTION ----------------
header_html = """
<div class="header-box" style="
    background: linear-gradient(135deg, #ffffff, #faf0ff);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
    text-align: center;
">

    <!-- SCHOOL LOGO -->
    <img src="https://www.schoolmykids.com/smk-media/2019/01/Amrita-Vidyalayam-Bangalore.png"
         style="width:160px; border-radius:15px; margin-bottom:10px;" />

    <!-- TITLE -->
    <h1 style="color:#8A2BE2; font-weight:900; margin-top:10px;">
        Welcome to the Computer Expo 2025 🎉
    </h1>

    <!-- SUBTITLE -->
    <h2 style="color:#FF1493; margin-top:-10px;">
        Amrita Vidyalayam
    </h2>

    <!-- SMALL TEXT -->
    <h4 style="color:#444; margin-top:-5px;">
        A Creative Project by Grade 7 Students 💻✨
    </h4>

    <!-- ROBOT ICON -->
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712100.png"
         style="width:110px; margin-top:10px;" />

</div>
"""

st.markdown(header_html, unsafe_allow_html=True)



# ---------------- FORM ----------------
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox("🎨 Your Favourite Color",
                     ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"])

# ---------------- FUTURE MESSAGES ----------------
messages = {
    "Red": (
        "🔥 You are bold, passionate, and full of unstoppable energy! "
        "Your future holds adventures, leadership, and powerful achievements."
    ),
    "Blue": (
        "🌊 Calm, intelligent, peaceful — your mind is your superpower! "
        "Great success in academics and creativity awaits you."
    ),
    "Green": (
        "🌿 Kind-hearted and caring — you bring harmony wherever you go. "
        "Your future will touch lives and inspire positivity."
    ),
    "Yellow": (
        "🌟 Bright, cheerful, creative — you make every place better! "
        "A fun, imaginative, and successful journey lies ahead."
    ),
    "Purple": (
        "🔮 Unique and imaginative — your ideas can change the world. "
        "Your future is full of innovation and brilliance."
    ),
    "Pink": (
        "💖 Loving and joyful — people feel happy around you. "
        "Your future will be full of friendships and heartwarming moments."
    ),
    "Black": (
        "⚫ Strong, focused, determined — you never give up! "
        "A powerful and successful path is waiting for you."
    ),
    "White": (
        "🤍 Pure, calm, peaceful — you bring comfort and clarity. "
        "A serene, graceful, and inspiring journey awaits."
    ),
}


# ---------------- SUBMIT BUTTON ----------------
if st.button("✨ Reveal My Future"):
    if name == "" or city == "":
        st.error("Please fill all fields!")
    else:
        msg = messages[color]
        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        df = pd.read_csv(CSV_FILE)

        new_row = {
            "Name": name,
            "Age": age,
            "City": city,
            "Favorite Color": color,
            "Message": msg
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        st.success("Your response has been saved! 📘")


# ---------------- ADMIN PANEL ----------------
st.write("---")
st.header("🔒 Admin Access Only")

admin_pw = st.text_input("Enter admin password:", type="password")

if st.button("🔐 Login"):
    if admin_pw == ADMIN_PASSWORD:
        st.success("Admin login successful!")

        df = pd.read_csv(CSV_FILE)
        st.dataframe(df)

        st.download_button(
            label="📥 Download CSV Data",
            data=df.to_csv(index=False),
            file_name="futurecolor_data.csv",
            mime="text/csv",
        )
    else:
        st.error("❌ Incorrect password")

# ---------------- FOOTER ----------------
st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
