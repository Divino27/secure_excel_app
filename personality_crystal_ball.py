import streamlit as st
import pandas as pd
import os

# ----------------------------------------------------
# PAGE SETTINGS
# ----------------------------------------------------
st.set_page_config(
    page_title="Future Color Bot - Computer Expo",
    page_icon="🎨",
    layout="centered"
)

# ----------------------------------------------------
# ADMIN PASSWORD
# ----------------------------------------------------
ADMIN_PASSWORD = "amrita123@"   # CHANGE IF YOU WANT

# ----------------------------------------------------
# CLOUD CSV FILE
# ----------------------------------------------------
CSV_FILE = "futurecolor_data.csv"

# Create CSV if not exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_csv(CSV_FILE, index=False)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------
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
    width: 110px;
    margin-top: -10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

amrita_logo = "/mnt/data/13cf8c6e-fc5c-4e48-992a-02f728719cf0.png"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"

st.markdown("<div class='header-box'>", unsafe_allow_html=True)

if os.path.exists(amrita_logo):
    st.image(amrita_logo, width=150)

st.markdown("""
<h1 style="color:#8A2BE2; font-weight:900;">Welcome to the Computer Expo 2025 🎉</h1>
<h2 style="color:#FF1493;">Amrita Vidyalayam</h2>
<h4 style="color:#333;">A Creative Project by Grade 7 Students 💻✨</h4>
""", unsafe_allow_html=True)

st.markdown(f"<img src='{robot_image}' class='robot-image'>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# USER INPUT FORM
# ----------------------------------------------------
st.header("🎨 Discover Your Future Through Your Favourite Color!")

name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=3, max_value=100)
city = st.text_input("🏙️ Your City")

color = st.selectbox(
    "🎨 Choose Your Favourite Color:",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
)

# ----------------------------------------------------
# FUTURE MESSAGES FOR COLORS
# ----------------------------------------------------
messages = {
    "Red": (
        "🔥 You are bold, passionate, and full of unstoppable energy!\n\n"
        "Your future is filled with exciting adventures and leadership opportunities.\n"
        "People naturally admire your confidence. Big achievements await you!"
    ),

    "Blue": (
        "🌊 Calm, intelligent, and thoughtful — you bring peace wherever you go.\n\n"
        "Your future shows success in academics and creative thinking.\n"
        "You will solve complex problems and make wise decisions."
    ),

    "Green": (
        "🌿 You have a gentle heart and a peaceful mind.\n\n"
        "Your future shines brightly with kindness and harmony.\n"
        "You will inspire people with your positivity and caring nature."
    ),

    "Yellow": (
        "🌟 Cheerful and creative — your imagination is powerful!\n\n"
        "Your future is full of fun experiences, ideas, and innovation.\n"
        "You brighten every place you enter — keep shining!"
    ),

    "Purple": (
        "🔮 Unique, imaginative, and a deep thinker.\n\n"
        "Your future holds extraordinary accomplishments.\n"
        "Your ideas will create new possibilities in the world."
    ),

    "Pink": (
        "💖 Loving, joyful, and full of kindness.\n\n"
        "Your future is full of happy moments and strong friendships.\n"
        "People enjoy your presence and feel loved around you."
    ),

    "Black": (
        "⚫ Strong, focused, and determined.\n\n"
        "Your future holds leadership, discipline, and massive achievements.\n"
        "You can stay calm under pressure — a true achiever!"
    ),

    "White": (
        "🤍 Pure-hearted, calm, and peaceful.\n\n"
        "Your future is full of clarity and balance.\n"
        "You will bring harmony and inspiration to everyone around you."
    )
}

# ----------------------------------------------------
# SUBMIT BUTTON
# ----------------------------------------------------
if st.button("✨ Reveal My Future"):
    if name.strip() == "" or city.strip() == "":
        st.error("Please fill all the details!")
    else:
        msg = messages[color]
        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to CSV
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

        st.success("Your future prediction is saved securely! 📘")

# ----------------------------------------------------
# ADMIN PANEL
# ----------------------------------------------------
st.write("---")
st.header("🔒 Admin Access Only")

admin_pw = st.text_input("Enter admin password:", type="password")

if st.button("🔐 Login"):
    if admin_pw == ADMIN_PASSWORD:
        st.success("Admin access granted!")

        df = pd.read_csv(CSV_FILE)
        st.dataframe(df)

        st.download_button(
            label="📥 Download Color Bot Data (CSV)",
            data=open(CSV_FILE, "rb").read(),
            file_name="futurecolor_data.csv",
            mime="text/csv"
        )
    else:
        st.error("❌ Incorrect password")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
