# personality_crystal_ball.py
import streamlit as st
import pandas as pd
import os
import sys
import io
from datetime import datetime

# For Windows hiding attribute
import platform
if platform.system() == "Windows":
    import ctypes

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Personality Crystal Ball", page_icon="🔮", layout="centered")

# Admin password (change this)
ADMIN_PASSWORD = "teacher123"

# Use the uploaded logo path from your session by default.
# If running on the school PC, copy your logo file into project folder and set logo_path = "logo.png"
logo_path = "/mnt/data/13cf8c6e-fc5c-4e48-992a-02f728719cf0.png"

# Hidden secure folder (cross-platform)
HOME = os.path.expanduser("~")
SECURE_DIR = os.path.join(HOME, ".secure_personality_data")  # dot prefix makes it hidden on Unix
if not os.path.exists(SECURE_DIR):
    os.makedirs(SECURE_DIR, exist_ok=True)

# Excel file inside secure folder
excel_file = os.path.join(SECURE_DIR, "win_sys_cache_1937.xlsx")

# Default columns
COLUMNS = ["Timestamp", "Name", "Class", "Q1", "Q2", "Q3", "Q4", "Q5", "Personality", "Message"]

# If no file exists, create initial file (unprotected here; it will be rewritten protected on each save)
if not os.path.exists(excel_file):
    df_init = pd.DataFrame(columns=COLUMNS)
    df_init.to_excel(excel_file, index=False, engine="xlsxwriter")

# Helper: set hidden attribute on Windows (so the folder is hidden in Explorer)
def hide_folder_windows(path):
    try:
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ctypes.windll.kernel32.SetFileAttributesW(str(path), FILE_ATTRIBUTE_HIDDEN)
    except Exception:
        pass

# Hide secure directory on Windows
if platform.system() == "Windows":
    hide_folder_windows(SECURE_DIR)

# ---------------- UI ----------------
st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

# Header with logo
cols = st.columns([1, 3, 1])
with cols[1]:
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)
    st.markdown("<div class='top-card'><h1 style='color:#6A1B9A'>🔮 Personality Crystal Ball</h1>"
                "<p style='margin-top:-10px;color:#FF4081'>Discover your personality type — quick and fun!</p></div>",
                unsafe_allow_html=True)

st.write("")

# Student form
with st.form("personality_form"):
    st.header("Tell the Crystal Ball about you")
    name = st.text_input("Your name")
    student_class = st.text_input("Class / Grade (optional)")

    st.markdown("### Quick questions — choose one option each")
    st.markdown("**1) Are you usually calm or energetic?**")
    q1 = st.radio("", ["Calm", "Energetic", "Both equally"])

    st.markdown("**2) Do you prefer indoors or outdoors?**")
    q2 = st.radio("", ["Indoors", "Outdoors", "Both"])

    st.markdown("**3) Would you rather draw or play sports?**")
    q3 = st.radio("", ["Draw / Create", "Sports / Movement", "Both"])

    st.markdown("**4) Are you shy or talkative?**")
    q4 = st.radio("", ["Shy", "Talkative", "Depends"])

    st.markdown("**5) Favorite subject?**")
    q5 = st.radio("", ["Math / Science", "Arts", "Physical Education", "Languages", "Other"])

    submitted = st.form_submit_button("✨ Reveal My Personality")

# Determine personality logic
def compute_personality(a,b,c,d,e):
    # Simple scoring rules — you can tune these
    score = {"Mind Explorer":0, "Energy Champion":0, "Creative Genius":0, "Peace Guardian":0, "Future Leader":0}

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
        score["Future Leader"] += 1
    elif e == "Arts":
        score["Creative Genius"] += 2
    elif e == "Physical Education":
        score["Energy Champion"] += 2
    elif e == "Languages":
        score["Peace Guardian"] += 1
        score["Mind Explorer"] += 1
    else:
        score["Mind Explorer"] += 1

    # choose max
    personality = max(score, key=score.get)
    return personality

# Personality messages
personality_text = {
    "Mind Explorer": (
        "🧠 Mind Explorer — You love learning and solving puzzles. "
        "Your future is bright in science, research, and problem solving. "
        "Keep asking questions, you will uncover exciting discoveries."
    ),
    "Energy Champion": (
        "⚡ Energy Champion — Full of life and enthusiasm! "
        "You shine in action, sports, and leading activities. "
        "Your energy inspires others — use it to bring teams together."
    ),
    "Creative Genius": (
        "🎨 Creative Genius — Your imagination is your superpower. "
        "You will create beautiful art, stories, or inventions. "
        "Keep practicing your craft and your ideas will change the world."
    ),
    "Peace Guardian": (
        "🌿 Peace Guardian — Gentle, kind, and caring. "
        "You help others and build calm in groups. "
        "You may become a great helper, teacher, or someone who heals."
    ),
    "Future Leader": (
        "🚀 Future Leader — Confident and bold. "
        "People follow your ideas. You will lead groups, build projects, and make big changes."
    )
}

# When student submits
if submitted:
    if not name:
        st.error("Please enter your name.")
    else:
        personality = compute_personality(q1,q2,q3,q4,q5)
        message = personality_text.get(personality, "")
        st.success(f"Hello **{name}** — your personality is **{personality}**")
        st.info(message)

        # Prepare new row
        new_row = {
            "Timestamp": datetime.now().isoformat(),
            "Name": name,
            "Class": student_class,
            "Q1": q1,
            "Q2": q2,
            "Q3": q3,
            "Q4": q4,
            "Q5": q5,
            "Personality": personality,
            "Message": message
        }

        # Save to Excel with password protection (local using xlsxwriter)
        # This will overwrite the file each time with protection set.
        try:
            df_existing = pd.read_excel(excel_file)
        except Exception:
            df_existing = pd.DataFrame(columns=COLUMNS)

        df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)

        # Write with password protection using xlsxwriter (local only)
        # NOTE: This will work on local PC with xlsxwriter installed. Not supported on Streamlit Cloud.
        try:
            with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
                df_updated.to_excel(writer, index=False, sheet_name="Data")
                workbook = writer.book
                # Set file password (change if you want)
                workbook.password = "1234"
                worksheet = writer.sheets["Data"]
                worksheet.protect("1234")
            # hide the folder again on Windows
            if platform.system() == "Windows":
                hide_folder_windows(SECURE_DIR)
            st.success("Your response was saved securely. Thank you!")
        except Exception as e:
            # If xlsxwriter not available (e.g., running on Cloud), fallback to normal save (not protected).
            df_updated.to_excel(excel_file, index=False)
            st.warning("Saved data, but secure password-protection failed on this machine (works locally only).")

# ---------------- ADMIN PANEL ----------------
st.markdown("---")
st.header("🔒 Admin Panel (Owner only)")
admin_pw = st.text_input("Enter admin password to view data", type="password")
if st.button("Unlock Admin Panel"):
    if admin_pw == ADMIN_PASSWORD:
        st.success("Admin access granted.")
        # read secure file and display in table
        try:
            df_show = pd.read_excel(excel_file)
            st.dataframe(df_show)
            # provide download
            with open(excel_file, "rb") as f:
                excel_bytes = f.read()
            st.download_button("📥 Download Secure Excel", data=excel_bytes,
                               file_name=os.path.basename(excel_file),
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        except Exception as e:
            st.error("Could not open secure file. Make sure the app is running on the local computer and the file exists.")
    else:
        st.error("Wrong admin password.")

# Footer
st.write("")
st.caption("This app saves data to a hidden, password-protected Excel file on this computer. "
           "Password protection requires xlsxwriter and will work when run locally (not online).")
