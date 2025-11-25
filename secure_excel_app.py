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

.header-box {
    background: rgba(255,255,255,0.92);
    padding: 28px;
    border-radius: 25px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.22);
    text-align: center;
    margin-bottom: 25px;
}

.top-image {
    width: 200px;
    margin-bottom: 10px;
    border-radius: 20px;
}

.robot-image {
    width: 120px;
    margin-top: -15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
fun_image = "https://yt3.ggpht.com/ytc/AIdro_lNE9F1qUp8GvAxWoWy67enscUnKgwEB5Rj00Fm35aa-w=s800"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"

st.markdown(f"""
<div class="header-box">
    <img src="{fun_image}" class="top-image">
    <h1 style="color:#8A2BE2; font-weight:900;">Welcome to the Computer Expo 2025 🎉</h1>
    <h2 style="color:#FF1493;">Amrita Vidyalayam</h2>
    <h4 style="color:#333;">A Creative Project by V. Madhavan, 7A 💻✨</h4>
    <img src="{robot_image}" class="robot-image">
</div>
""", unsafe_allow_html=True)

# ---------------- EXCEL SETUP ----------------
excel_file = "futurecolor_data.xlsx"

if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_excel(excel_file, index=False)

# ---------------- FORM ----------------
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox(
    "🎨 Your Favourite Color",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
)

# ---------------- FUTURE MESSAGES ----------------
messages = {
    "Red": "🔥 You are bold and passionate! Big adventures await you.",
    "Blue": "🌊 Calm and intelligent — academic success is in your future!",
    "Green": "🌿 Kind-hearted and peaceful — you will inspire many people.",
    "Yellow": "🌟 Cheerful and creative — amazing ideas are coming your way!",
    "Purple": "🔮 Unique thinker — you will shine in unexpected ways!",
    "Pink": "💖 Positive and loving — people enjoy being around you.",
    "Black": "⚫ Strong, focused, and determined — success is guaranteed.",
    "White": "🤍 Calm and pure — you bring peace wherever you go."
}

# ---------------- SUBMIT BUTTON ----------------
if st.button("✨ Reveal My Future"):
    if name == "" or city == "":
        st.error("Please fill all fields!")
    else:
        msg = messages[color]

        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to Excel (works on Cloud)
        df = pd.read_excel(excel_file)
        new_row = {
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(excel_file, index=False)

        st.success("Your response has been saved to Excel! 📘")

# ---------------- DOWNLOAD BUTTON ----------------
with open(excel_file, "rb") as f:
    excel_bytes = f.read()

st.download_button(
    label="📥 Download Visitor Excel Data",
    data=excel_bytes,
    file_name="futurecolor_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ---------------- FOOTER ----------------
st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
