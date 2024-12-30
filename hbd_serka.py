import pandas as pd
from datetime import datetime
import streamlit as st

# Judul Aplikasi
st.title("🎀 𝒟𝒶𝓉𝒶 𝒰𝓁𝒶𝓃𝑔 𝒯𝒶𝒽𝓊𝓃 🎀")

# Path ke file Excel
file_path = 'https://raw.githubusercontent.com/euforiaserka/habede/refs/heads/main/hbd_serka_csv.csv'

# Membaca data dari Excel
df = pd.read_csv(file_path)

# Mendapatkan tanggal hari ini
today = datetime.today()

# Memisahkan kolom Tanggal Lahir menjadi bulan, hari, dan tahun
df['Bulan'] = pd.to_datetime(df['Tanggal Lahir']).dt.month
df['Hari'] = pd.to_datetime(df['Tanggal Lahir']).dt.day

# Filter data untuk mencari yang berulang tahun hari ini
ulang_tahun_hari_ini = df[(df['Bulan'] == today.month) & (df['Hari'] == today.day)]

# Memilih hanya kolom 'Nama Lengkap', 'NIM', 'Foto', dan 'PJ'
selected_columns = ['Nama Lengkap', 'NIM', 'Foto Diri Bebas', 'PJ']
data_terpilih = ulang_tahun_hari_ini[selected_columns]

# Menampilkan hasil
if not ulang_tahun_hari_ini.empty:
    st.header("Orang yang berulang tahun hari ini:")
    st.dataframe(data_terpilih)
else:
    st.header("\nYeay, Ga ada yang berulang tahun hari ini 😉\n")

st.header('\nJangan Lupa Screenshoot yahh cintaaa 🫶\n1. Bukti Post: https://drive.google.com/drive/folders/1QW179Y_dbuXzRAoAigmDT-T-yZMQLdAt?usp=sharing\n\n2. Bukti Makasih: https://drive.google.com/drive/folders/1mwu69EvDQ6gs1Gif6VYMNifayrBJOTjI?usp=sharing\n')
st.subheader('\n🎴Template HBD:\n1. https://www.canva.com/design/DAGGKaTKLRg/NH4lCpdlU9CBvz7rwSQhqg/edit?utm_content=DAGGKaTKLRg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton\n2. https://www.canva.com/design/DAGGn3yDVZc/ffOZj-PPW0ivQbDjHv3cxg/edit?utm_content=DAGGn3yDVZc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton\n')
st.subheader('\n📸Template Caption:\nhttps://docs.google.com/document/d/1fx1yuuWmBXkMBBdu7bBFaHX48fD9HxeVdKiveeHkMNs/edit?usp=sharing\n')
st.subheader('\n📥Link Request Publikasi\nhttps://bit.ly/ArunikaPublikasi\n')
st.text('\nSemangat yaa anak-anakku :)')
