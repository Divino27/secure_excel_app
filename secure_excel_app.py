import pandas as pd
import os

# ---------------- SETTINGS ----------------
excel_file = "secure_futurecolor_data.xlsx"
password = "1234"   # 🔐 CHANGE PASSWORD HERE


# ---------------- CREATE INITIAL FILE ----------------
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_excel(excel_file, index=False, engine="xlsxwriter")

# ---------------- ASK USER INPUT ----------------
print("\nWELCOME TO FUTURECOLOR SECURE APP")
print("-----------------------------------")

name = input("Enter your Name: ")
age = input("Enter your Age: ")
city = input("Enter your City: ")

print("\nChoose a Color:")
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
for i, c in enumerate(colors, start=1):
    print(f"{i}. {c}")

choice = int(input("Enter option number: "))
color = colors[choice - 1]

# ---------------- FUTURE MESSAGES ----------------
messages = {
    "Red": "You are bold and passionate. Great adventures await you!",
    "Blue": "You are calm and intelligent. Academic success is ahead!",
    "Green": "You are peaceful and kind. You inspire everyone!",
    "Yellow": "You are cheerful and creative. Amazing ideas will bloom!",
    "Purple": "You are unique and imaginative. Extraordinary success awaits!",
    "Pink": "You are positive and loving. Happiness follows you everywhere!",
    "Black": "You are strong and determined. Success is guaranteed!",
    "White": "You are calm and pure. You bring peace wherever you go!"
}

msg = messages[color]

print("\nYour Future Message:")
print(msg)

# ---------------- SAVE TO PASSWORD PROTECTED EXCEL ----------------
df_existing = pd.read_excel(excel_file)

new_row = {
    "Name": name,
    "Age": age,
    "City": city,
    "Favorite Color": color,
    "Message": msg
}

df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)

# Write to Excel with password
with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
    df_updated.to_excel(writer, index=False, sheet_name="Data")
    
    workbook = writer.book
    worksheet = writer.sheets["Data"]

    # Apply password protection 🔐
    workbook.password = password
    worksheet.protect(password=password)


print(f"\n✔ Data saved securely to {excel_file}")
print("✔ Excel file is password protected")
print(f"🔐 Password: {password}")
print("\nDONE!")
