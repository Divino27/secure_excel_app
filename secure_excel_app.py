import streamlit as st
import pandas as pd
import os
import xlsxwriter  # Works only on local PC, not Streamlit Cloud

st.set_page_config(page_title="Secure Excel App", page_icon="🔐")

st.title("🔐 Password-Protected Excel Saver")
st.write("This app saves your data in a password-protected Excel file.")

excel_file = "secure_data.xlsx"
password = "1234"   # You can change this

# Create empty Excel if not existing
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Class", "City"])
    df.to_excel(excel_file, index=False)

# Form
name = st.text_input("👤 Name")
grade = st.text_input("🏫 Class / Grade")
city = st.text_input("🌍 City")

if st.button("Save to Secure Excel"):
    if name == "" or grade == "" or city == "":
        st.error("Please fill all fields!")
    else:
        df = pd.read_excel(excel_file)
        new_row = {"Name": name, "Class": grade, "City": city}

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # Save with password protection
        with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Data")
            workbook = writer.book
            workbook.password = password

        st.success(f"Data saved successfully! 🔐 Password = {password}")

# Download Button
with open(excel_file, "rb") as f:
    st.download_button(
        label="📥 Download Secure Excel",
        data=f.read(),
        file_name="secure_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
