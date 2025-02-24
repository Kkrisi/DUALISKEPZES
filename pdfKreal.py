import os
import random
from datetime import datetime
from fpdf import FPDF

# Véletlenszerű névlista
nevek = ["Kis Pista", "Nagy János", "Szabó Erika", "Tóth Béla", "Kovács Anna",
         "Horváth Zoltán", "Varga István", "Kiss Ágnes", "Molnár Ferenc", "Németh Júlia"]

# Email domain lista
email_domainok = ["mail.com", "gmail.com", "yahoo.com", "example.com"]

# Aktuális dátum/idő formátuma
def jelenlegi_ido():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Véletlenszerű email generálás
def email_keszites(nev):
    keresztnev, vezeteknev = nev.split(" ")
    # 5 darab '&' karaktert generálunk a név elé
    special_prefix = '&' * 5
    return f"{special_prefix}{keresztnev.lower()}.{vezeteknev.lower()}@{random.choice(email_domainok)}"

# PDF generálása
def generate_pdf(filename, output_dir):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Ez egy generált PDF fájl.", ln=True, align="C")
    
    # Mentés az output mappába
    full_path = os.path.join(output_dir, filename)
    pdf.output(full_path)

# Mappa létrehozása a PDF fájloknak
output_dir = "tomegpelda"
os.makedirs(output_dir, exist_ok=True)

# SQL sorok gyűjtése
sql_sorok = []

# 100 PDF fájl és SQL sor generálása
for _ in range(100):
    # Véletlenszerű név kiválasztása
    nev = random.choice(nevek)
    
    # Véletlenszerű student_id generálása (ez kerül a fájlnévbe is)
    student_id = random.randint(10000, 99999)
    
    # Email generálása
    email = email_keszites(nev)
    
    # Dátumok
    created_at = jelenlegi_ido()
    updated_at = created_at
    
    # PDF fájlnév generálása
    random_7_digit = random.randint(1000000, 9999999)
    datum = datetime.now().strftime("%Y%m%d")
    pdf_filename = f"Jövedelemkifizetési lap - {nev}         ({student_id})  {datum}_{random_7_digit}.pdf"
    
    # PDF fájl generálása
    generate_pdf(pdf_filename, output_dir)
    
    # SQL sor összeállítása
    sql_sor = f"({student_id}, '{email}', '{nev}', '{created_at}', '{updated_at}')"
    sql_sorok.append(sql_sor)

# SQL INSERT INTO lekérdezés
sql_insert = "INSERT INTO students (student_id, email, nev, created_at, updated_at) VALUES\n" + ",\n".join(sql_sorok) + ";"

# SQL kiírás fájlba
sql_file_path = "insert_students.sql"
with open(sql_file_path, "w", encoding="utf-8") as file:
    file.write(sql_insert)

print(f"100 PDF fájl elkészült a '{output_dir}' mappában.")
print(f"SQL utasítások mentve a '{sql_file_path}' fájlba.")
