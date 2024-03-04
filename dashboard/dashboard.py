import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='ticks')


# Memuat data gabungan dari file CSV
all_df = pd.read_csv("all_data.csv")

# Menampilkan judul
st.title("Bike Sharing Dashboard")

# Menampilkan beberapa baris pertama data
st.subheader("Data Preview")
st.write(all_df.head())

# Menampilkan statistik deskriptif
st.subheader("Descriptive Statistics")
st.write(all_df.describe())

# ====================== Opening ==============================================

# Memisahkan data berdasarkan tahun
data_2011 = all_df[all_df['yr_x'] == 0] # 2011
data_2012 = all_df[all_df['yr_x'] == 1] # 2012

grouped_season_2011 = data_2011.groupby('season_x')['cnt_x'].sum()
grouped_season_2012 = data_2012.groupby('season_x')['cnt_x'].sum()

st.subheader("Peningkatan tren peminjaman sepeda pada tahun 2011 dan 2012")
# Membuat plot menggunakan Matplotlib
plt.figure(figsize=(10, 6))

plt.plot(grouped_season_2011.index, grouped_season_2011.values, marker='o', label='2011')
plt.plot(grouped_season_2012.index, grouped_season_2012.values, marker='o', label='2012')

plt.title('Peningkatan Tren Peminjaman Sepeda antara Tahun 2011 dan 2012')
plt.xlabel('Musim')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.legend()
plt.grid(True)

# Menampilkan plot dalam Streamlit dashboard
st.pyplot(plt)

# Menampilkan plot hubungan antara 'temp' dan 'cnt'
st.subheader("Korelasi antara Temperature dan Jumlah Peminjaman")
st.scatter_chart(all_df[['temp_x', 'cnt_x']])

# =================================================================== #
# 1.1. Mencari analisis peminjaman sepeda bedasarkan musim

# Membuat fungsi untuk menghitung persentase
def hitung_persentase(jumlah, total):
    return (jumlah / total) * 100

# Menghitung total peminjaman sepeda untuk semua musim
total_peminjaman_semua_musim = all_df['cnt_x'].sum()

# Menghitung total peminjaman sepeda untuk setiap musim
grouped_season = all_df.groupby('season_x')
total_rental_per_season = grouped_season['cnt_x'].sum()

# Menampilkan jumlah peminjaman sepeda untuk setiap musim
st.subheader("Jumlah Peminjaman Sepeda per Musim")
for season, total_rentals in total_rental_per_season.items():
    if season == 1:
        st.write("Musim semi:", total_rentals, "orang")
    elif season == 2:
        st.write("Musim panas:", total_rentals, "orang")
    elif season == 3:
        st.write("Musim gugur:", total_rentals, "orang")
    elif season == 4:
        st.write("Musim dingin:", total_rentals, "orang")

# Menghitung persentase peminjaman sepeda untuk setiap musim
season_labels = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
percentages = []
for season, total_rentals in total_rental_per_season.items():
    percentage = round((total_rentals / total_peminjaman_semua_musim) * 100, 2)
    percentages.append(percentage)

# Membuat plot pie chart
fig, ax = plt.subplots()
ax.pie(percentages, labels=season_labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
st.title('1. Persentase Peminjaman Sepeda per Musim')
ax.axis('equal')  # Membuat lingkaran menjadi lingkaran sempurna
st.pyplot(fig)

# =============================================================================== #

# 1.2. Membuat analisis Total peminjaman sepeda pada 2011 dan 2012

# Memisahkan data berdasarkan tahun
data_2011 = all_df[all_df['yr_x'] == 0] # 2011
data_2012 = all_df[all_df['yr_x'] == 1] # 2012

# ================================================================================ #

# 1.2.1 Mengelompokkan data untuk tahun 2011 berdasarkan musim

grouped_season_2011 = data_2011.groupby('season_x')
total_rental_per_season_2011 = grouped_season_2011['cnt_x'].sum()


# Menampilkan data peminjaman sepeda per musim untuk tahun 2011
st.subheader("1.1. Peminjaman Sepeda per Musim untuk Tahun 2011")
for season, total_rentals in total_rental_per_season_2011.items():
    if season == 1:
        st.write("Musim semi:", total_rentals, "orang")
    elif season == 2:
        st.write("Musim panas:", total_rentals, "orang")
    elif season == 3:
        st.write("Musim gugur:", total_rentals, "orang")
    elif season == 4:
        st.write("Musim dingin:", total_rentals, "orang")

# Data jumlah peminjaman sepeda per musim tahun 2011
seasons_2011 = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
total_rentals_2011 = [total_rentals for season, total_rentals in total_rental_per_season_2011.items()]

# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(seasons_2011, total_rentals_2011, color='lightgreen')
ax.set_title('Jumlah Peminjaman Sepeda per Musim Tahun 2011')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Peminjaman Sepeda')
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Menghitung total peminjaman sepeda untuk semua musim pada tahun 2011
total_peminjaman_semua_musim_2011 = sum(total_rentals_2011)

# Data persentase peminjaman sepeda untuk tiap musim pada tahun 2011
seasons = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
percentages = []

# Menghitung persentase peminjaman sepeda untuk tiap musim pada tahun 2011
st.subheader("1.2. Persentase peminjaman sepeda tiap musim pada 2011:")
for season, total_rentals in total_rental_per_season_2011.items():
    persentase = round((total_rentals / total_peminjaman_semua_musim_2011) * 100, 2)
    percentages.append(persentase)
    if(season == 1):
        st.write(f"musim semi\t: {persentase}%")
    elif(season == 2):
        st.write(f"musim panas\t: {persentase}%")
    elif(season == 3):
        st.write(f"musim gugur\t: {persentase}%")
    elif(season == 4):
        st.write(f"musim dingin\t: {persentase}%")
    

# Membuat plot pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, labels=seasons, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue'])
ax.set_title('Persentase Peminjaman Sepeda untuk Tiap Musim pada Tahun 2011')
ax.axis('equal')  # Membuat pie chart menjadi lingkaran
st.pyplot(fig)


# ============================================================================================ #

grouped_season_2012 = data_2012.groupby('season_x')
total_rental_per_season_2012 = grouped_season_2012['cnt_x'].sum()

st.subheader("1.4. Peminjaman Sepeda per Musim untuk Tahun 2012")
for season, total_rentals in total_rental_per_season_2012.items():
    if season == 1:
        st.write("Musim semi:", total_rentals, "orang")
    elif season == 2:
        st.write("Musim panas:", total_rentals, "orang")
    elif season == 3:
        st.write("Musim gugur:", total_rentals, "orang")
    elif season == 4:
        st.write("Musim dingin:", total_rentals, "orang")

# Data jumlah peminjaman sepeda per musim tahun 2012
seasons_2012 = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
total_rentals_2012 = [total_rentals for season, total_rentals in total_rental_per_season_2011.items()]

# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(seasons_2012, total_rentals_2012, color='lightgreen')
ax.set_title('Jumlah Peminjaman Sepeda per Musim Tahun 2012')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Peminjaman Sepeda')
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Menghitung total peminjaman sepeda untuk semua musim pada tahun 2011
total_peminjaman_semua_musim_2012 = sum(total_rentals_2012)

# Data persentase peminjaman sepeda untuk tiap musim pada tahun 2011
seasons = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
percentages = []

# Menghitung persentase peminjaman sepeda untuk tiap musim pada tahun 
st.subheader("1.5. Persentase peminjaman sepeda tiap musim pada 2012:")
for season, total_rentals in total_rental_per_season_2012.items():
    persentase = round((total_rentals / total_peminjaman_semua_musim_2012) * 100, 2)
    percentages.append(persentase)
    if(season == 1):
        st.write(f"musim semi\t: {persentase}%")
    elif(season == 2):
        st.write(f"musim panas\t: {persentase}%")
    elif(season == 3):
        st.write(f"musim gugur\t: {persentase}%")
    elif(season == 4):
        st.write(f"musim dingin\t: {persentase}%")
    

# Membuat plot pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, labels=seasons, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue'])
ax.set_title('Persentase Peminjaman Sepeda untuk Tiap Musim pada Tahun 2012')
ax.axis('equal')  # Membuat pie chart menjadi lingkaran
st.pyplot(fig)

# ========================================================================================================== #

# 2.1 ========================== 2.1 =============================== 2.1 ==============

# Menampilkan total peminjaman sepeda berdasarkan jam
grouped_hour = all_df.groupby('hr')
total_rentals_per_hour = grouped_hour['cnt_y'].sum()

# Menampilkan judul
st.title("2. Total Peminjaman Sepeda Berdasarkan Jam")

# Menampilkan total peminjaman sepeda berdasarkan jam
st.subheader("2.1. Total Peminjaman Sepeda Berdasarkan Jam")

# Menampilkan jumlah peminjaman sepeda tiap jam per hari
hourly_rentals = all_df.groupby(by="hr")['cnt_y'].sum()

# Membuat plot histogram
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(hourly_rentals.index, hourly_rentals.values, color='lightgreen')
ax.set_title('Jumlah Peminjaman Sepeda Tiap Jam per Hari')
ax.set_xlabel('Jam (Hour)')
ax.set_ylabel('Jumlah Peminjaman Sepeda')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xticks(range(24))
st.pyplot(fig)

# ====================================================================================== #
# 2.2 ===================================== 2.2 =================================== 2.2 ==========
# Pengelompokan berdasarkan waktu 
st.subheader("2.2. Persentase peminjaman sepeda berdasarkan kategori waktu")

# Mengubah nilai jam (hour) 0 menjadi 24 untuk kemudahan perhitungan
all_df['hr'] = all_df['hr'].replace({0: 24})

# Membuat fungsi untuk mengelompokkan waktu dalam kategori yang ditentukan
def categorize_time(hr):
    if 5 <= hr <= 10:
        return 'Pagi'
    elif 11 <= hr <= 14:
        return 'Siang'
    elif 15 <= hr <= 18:
        return 'Sore'
    elif 19 <= hr <= 24:
        return 'Malam'
    elif 1 <= hr <= 4:
        return 'Dini Hari'

# Mengelompokkan data berdasarkan kategori waktu
all_df['Time_Category'] = all_df['hr'].apply(categorize_time)

# Mengelompokkan data berdasarkan kategori waktu dan menghitung total peminjaman sepeda
rentals_by_time = all_df.groupby('Time_Category')['cnt_y'].sum()

# Menampilkan hasil
st.title("3. Jumlah Peminjaman Sepeda Berdasarkan Kategori Waktu")
st.write("Jumlah peminjaman sepeda berdasarkan kategori waktu:")
st.write(rentals_by_time)

# Membuat plot diagram batang
st.bar_chart(rentals_by_time)

# =============================================================================================== #

st.subheader("3.1. Persentase peminjaman sepeda berdasarkan kategori waktu")
# Menghitung persentase peminjaman sepeda untuk setiap kategori waktu
percent_rentals_by_time = (rentals_by_time / total_peminjaman_semua_musim) * 100


# Data persentase peminjaman sepeda untuk setiap kategori waktu
time_categories = percent_rentals_by_time.index.tolist()
percentages = percent_rentals_by_time.tolist()

# Membuat plot pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, labels=time_categories, autopct='%1.1f%%', startangle=140)
ax.set_title('Persentase Peminjaman Sepeda Berdasarkan Kategori Waktu')
ax.axis('equal')  # Membuat pie chart menjadi lingkaran
st.pyplot(fig)

# ==================================================================================================== #
st.subheader("3.2. Total peminjaman sepeda terhadap suhu")

# Menghitung original_temp

original_temp = all_df['temp_y']*41

# Menampilkan total peminjaman sepeda berdasarkan suhu
grouped_temp = all_df.groupby(original_temp)
total_rentals_by_temp = grouped_temp['cnt_y'].sum()

# Data jumlah peminjaman sepeda tiap jam per hari dan suhu
hourly_rentals_by_temp = all_df.groupby(original_temp)['cnt_y'].sum()

# Membuat plot line dengan Matplotlib
plt.figure(figsize=(12, 6))
hourly_rentals_by_temp.plot(kind='line', marker='o', color='skyblue')
plt.title('Total Jumlah Peminjaman Sepeda per Jam per Hari terhadap Suhu')
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.grid(True)

# Menampilkan plot menggunakan Streamlit
st.pyplot(plt)

# Copyright
st.caption('Copyright (c) Bani Adam Tampubolon')