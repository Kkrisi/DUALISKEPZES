import pandas as pd
import random
import string

# Véletlenszerű nevek generálása
def generate_name():
    first_names = ["Anna", "Béla", "Csaba", "Dóra", "Emese", "Ferenc", "Gábor", "Hanna", "István", "Judit"]
    last_names = ["Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Véletlenszerű azonosítószám generálása (5 számjegy)
def generate_id():
    return ''.join(random.choices(string.digits, k=5))

# Véletlenszerű email cím generálása
def generate_email(name):
    domains = ["example.com", "mail.com", "domain.hu"]
    name_part = name.lower().replace(" ", ".")
    return f"{name_part}@{random.choice(domains)}"

# Csak 3 adat generálása
num_records = 300
names, ids, emails = [], [], []

for _ in range(num_records):
    name = generate_name()
    names.append(name)
    ids.append(generate_id())
    emails.append(generate_email(name))

# DataFrame létrehozása
data = {
    "Név": names,             # Külön oszlop a neveknek
    "BérlapKód": ids,         # Külön oszlop a Bérlapkódoknak
    "Email": emails           # Külön oszlop az Email címeknek
}
df = pd.DataFrame(data)

# CSV fájl mentése
csv_filename = "adatok_300.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

# Most betöltjük a CSV fájlt és módosítjuk az első sort (oszlopokat)
df = pd.read_csv(csv_filename)  # Betöltjük a CSV fájlt

# Az első sor, azaz az oszlopcímek módosítása
df.columns = ["Név", "BérlapKód", "Email"]

# Mentés a módosított fájlba
df.to_csv(csv_filename, index=False, sep=';',encoding='utf-8-sig')

print(f"Sikeresen létrehoztuk és módosítottuk a CSV fájlt: {csv_filename}")
