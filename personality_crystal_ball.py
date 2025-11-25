import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="FutureColor Bot - Computer Expo",
    page_icon="🎉",
    layout="centered"
)

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
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.20);
    text-align: center;
    margin-bottom: 20px;
}

/* AMRITA LOGO */
.school-logo {
    width: 170px;
    border-radius: 15px;
    margin-bottom: 10px;
}

/* Robot image */
.robot-image {
    width: 120px;
    margin-top: -8px;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER WITH LOGO + TITLE ----------------

amrita_logo = "https://www.schoolmykids.com/smk-media/2019/01/Amrita-Vidyalayam-Boloor-Mangaluru.png"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"

st.markdown(f"""
<div class="header-box">

    <img src="{amrita_logo}" class="school-logo">

    <h1 style="color:#8A2BE2; font-weight:900; margin-top:10px;">
        Welcome to the Computer Expo 2025 🎉
    </h1>

    <h2 style="color:#FF1493; margin-top:-10px;">
        Amrita Vidyalayam
    </h2>

    <h4 style="color:#333; margin-top:-5px;">
        A Creative Project by Grade 7 Students 💻✨
    </h4>

    <img src="{robot_image}" class="robot-image">

</div>
""", unsafe_allow_html=True)

# ---------------- CSV SETUP ----------------
csv_file = "futurecolor_data.csv"

if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_csv(csv_file, index=False)

# ---------------- FORM ----------------
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox("🎨 Your Favourite Color",
                     ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"])

# ---------------- FUTURE MESSAGES ----------------
messages = {
    "Red": (
        "🔥 You are bold, passionate, and full of unstoppable energy!\n\n"
        "Your future is filled with exciting adventures and leadership opportunities.\n\n"
        "People naturally look up to you because of your confidence and strong personality.\n\n"
        "Whatever you dream of — sports, science, arts, or innovation — you will chase it with power!\n\n"
        "A bright and thrilling path awaits you!"
    ),
    "Blue": (
        "🌊 Calm, intelligent, and thoughtful — you bring peace wherever you go.\n\n"
        "Your future shows great success in academics and creative thinking.\n\n"
        "Because of your strong focus, you will solve complex problems and achieve amazing things.\n\n"
        "A future filled with knowledge and wisdom awaits you!"
    ),
    "Green": (
        "🌿 You have a gentle heart and a peaceful soul.\n\n"
        "Your future is filled with kindness, creativity, and emotional strength.\n\n"
        "You inspire many people with your calm nature and positivity.\n\n"
        "A beautiful, harmonious journey lies ahead!"
    ),
    "Yellow": (
        "🌟 Cheerful, bright, and full of brilliant ideas — you are a natural creator!\n\n"
        "Your life will be full of creativity, imagination, and joyful experiences.\n\n"
        "People love your positive energy — you make every place brighter!\n\n"
        "You will shine in art, innovation, and teamwork!"
    ),
    "Purple": (
        "🔮 You are unique, imaginative, and full of deep thoughts.\n\n"
        "Your ideas are powerful enough to change the world.\n\n"
        "Your future holds extraordinary success in creativity, strategy, and innovation."
    ),
    "Pink": (
        "💖 You are loving, joyful, and full of kindness.\n\n"
        "Your future is filled with friendships, laughter, and positivity.\n\n"
        "People enjoy being around you because you make them feel valued."
    ),
    "Black": (
        "⚫ Strong, focused, and determined — you never give up!\n\n"
        "Your future shows discipline, leadership, and huge achievements.\n\n"
        "You stay strong even in challenges — success is waiting for you!"
    ),
    "White": (
        "🤍 Pure-hearted, calm, and peaceful — you bring harmony everywhere.\n\n"
        "Your future has balance, emotional strength, and quiet success.\n\n"
        "You inspire others with your gentle and wise nature."
    )
}

# ---------------- SUBMIT BUTTON ----------------
if st.button("✨ Reveal My Future"):
    if name == "" or city == "":
        st.error("Please fill all fields!")
    else:
        msg = messages[color]
        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        df = pd.read_csv(csv_file)
        new_row = {
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(csv_file, index=False)

        st.success("Your response has been saved! 📘")

# ---------------- ADMIN PANEL ----------------
st.markdown("---")
st.subheader("🔒 Admin Access Only")

admin_pw = st.text_input("Enter admin password:", type="password")

if st.button("🔐 Login"):
    if admin_pw == "amrita123@":
        st.success("Admin login successful!")

        df = pd.read_csv(csv_file)
        st.dataframe(df)

        # Download button
        st.download_button(
            label="📥 Download CSV Data",
            data=open(csv_file, "rb").read(),
            file_name="futurecolor_data.csv",
            mime="text/csv"
        )
    else:
        st.error("❌ Incorrect password")

# ---------------- FOOTER ----------------
st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
