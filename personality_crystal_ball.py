# personality_crystal_ball.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Personality Crystal Ball", page_icon="🔮", layout="centered")

ADMIN_PASSWORD = "teacher123"   # change this anytime

# ---------------- LOGO ----------------
AMRITA_LOGO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbX9L1H1flI_yurVPT2bTbpCX7dAGPBJlt2g&s"

st.markdown(
    f"""
    <div style='text-align:center;'>
        <img src="{AMRITA_LOGO}" width="150">
        <h1 style='color:#6A1B9A;'>🔮 Personality Crystal Ball</h1>
        <h3 style='color:#FF4081;margin-top:-8px;'>Welcome to the Computer Expo • By Grade 7 Students</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CLOUD-SAFE HIDDEN CSV STORAGE ----------------
# Create hidden data file inside the app folder
DATA_FILE = ".hidden_personality_data.csv"

# Create the CSV if missing
if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=[
        "Timestamp", "Name", "Class", "Q1", "Q2", "Q3", "Q4", "Q5", "Personality", "Message"
    ])
    df_init.to_csv(DATA_FILE, index=False)

# ---------------- STYLES ----------------
st.markdown("""
<style>
.top-card {
    background: linear-gradient(135deg,#fff7f0,#fef6ff);
    padding:20px;
    border-radius:14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align:center;
}
.question {
    background: #ffffff;
    padding:12px;
    border-radius:10px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FORM ----------------
st.header("Tell the Crystal Ball about you 🔍")

with st.form("personality_form"):
    name = st.text_input("Your Name")
    student_class = st.text_input("Class / Grade")

    st.write("### Quick Questions")
    q1 = st.radio("1) Are you usually calm or energetic?",
                  ["Calm", "Energetic", "Both equally"])
    q2 = st.radio("2) Do you prefer indoors or outdoors?",
                  ["Indoors", "Outdoors", "Both"])
    q3 = st.radio("3) Would you rather draw or play sports?",
                  ["Draw / Create", "Sports / Movement", "Both"])
    q4 = st.radio("4) Are you shy or talkative?",
                  ["Shy", "Talkative", "Depends"])
    q5 = st.radio("5) Favorite subject?",
                  ["Math / Science", "Arts", "Physical Education", "Languages", "Other"])

    submitted = st.form_submit_button("✨ Reveal My Personality")

# ---------------- PERSONALITY LOGIC ----------------
def compute_personality(a,b,c,d,e):
    score = {"Mind Explorer":0, "Energy Champion":0, "Creative Genius":0,
             "Peace Guardian":0, "Future Leader":0}

    # Q1
    if a == "Calm":
        score["Peace Guardian"] += 2
        score["Mind Explorer"] += 1
    elif a == "Energetic":
        score["Energy Champion"] += 2
        score["Future Leader"] += 1
    else:
        score["Future Leader"] += 1
        score["Creative Genius"] += 1

    # Q2
    if b == "Indoors":
        score["Mind Explorer"] += 2
        score["Creative Genius"] += 1
    elif b == "Outdoors":
        score["Energy Champion"] += 2
    else:
        score["Peace Guardian"] += 1
        score["Creative Genius"] += 1

    # Q3
    if c == "Draw / Create":
        score["Creative Genius"] += 2
    elif c == "Sports / Movement":
        score["Energy Champion"] += 2
        score["Future Leader"] += 1
    else:
        score["Creative Genius"] += 1
        score["Energy Champion"] += 1

    # Q4
    if d == "Shy":
        score["Mind Explorer"] += 2
        score["Peace Guardian"] += 1
    elif d == "Talkative":
        score["Future Leader"] += 2
    else:
        score["Mind Explorer"] += 1
        score["Future Leader"] += 1

    # Q5
    if e == "Math / Science":
        score["Mind Explorer"] += 2
    elif e == "Arts":
        score["Creative Genius"] += 2
    elif e == "Physical Education":
        score["Energy Champion"] += 2
    elif e == "Languages":
        score["Peace Guardian"] += 1
        score["Mind Explorer"] += 1
    else:
        score["Mind Explorer"] += 1

    return max(score, key=score.get)

# Personality descriptions
personality_text = {
    "Mind Explorer": "🧠 You love learning and solving puzzles — your future is bright!",
    "Energy Champion": "⚡ Full of excitement and confidence — you inspire others!",
    "Creative Genius": "🎨 Your imagination shines — you will create amazing things!",
    "Peace Guardian": "🌿 Calm, kind, thoughtful — you make the world better.",
    "Future Leader": "🚀 Confident and bold — you will lead others successfully!"
}

# ---------------- SAVE RESULT ----------------
if submitted:
    if name.strip() == "":
        st.error("Please enter your name.")
    else:
        personality = compute_personality(q1,q2,q3,q4,q5)
        message = personality_text[personality]

        st.success(f"✨ **{name}**, you are a **{personality}**!")
        st.info(message)

        # Save to CSV (cloud-safe)
        df_existing = pd.read_csv(DATA_FILE)
        new_row = {
            "Timestamp": datetime.now().isoformat(),
            "Name": name,
            "Class": student_class,
            "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5,
            "Personality": personality,
            "Message": message
        }

        df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)
        df_updated.to_csv(DATA_FILE, index=False)

        st.success("Your response was saved securely! 🔐")

# ---------------- ADMIN PANEL ----------------
st.markdown("---")
st.header("🔒 Admin Panel (Owner only)")

admin_pw = st.text_input("Enter admin password", type="password")

if st.button("Unlock Admin Panel"):
    if admin_pw == ADMIN_PASSWORD:
        st.success("Admin access granted ✔")
        df = pd.read_csv(DATA_FILE)
        st.dataframe(df)

        st.download_button(
            "📥 Download CSV",
            df.to_csv(index=False),
            file_name="personality_data.csv",
            mime="text/csv"
        )
    else:
        st.error("Wrong admin password ❌")

# Footer
st.caption("Data is stored in a hidden CSV file. Only the owner can access it.")
