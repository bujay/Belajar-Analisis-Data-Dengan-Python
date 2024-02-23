# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px

# LOAD DATA
@st.cache(allow_output_mutation=True)
def load_data():
    # lokasi file
    data_day = pd.read_csv("../data/day.csv")
    data_hour = pd.read_csv("../data/hour.csv")
    return data_day, data_hour

data_day, data_hour = load_data()

# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Sharing Dashboard")

# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Ahmad Bujai Rimi**")
st.sidebar.markdown("**• Email: ahmadbujai20@gmail.com**")
st.sidebar.title("Dataset Bike Share")

# Show dataset in sidebar if toggled
if st.sidebar.checkbox("Show raw data", False):
    st.sidebar.write(data_day, data_hour)

# MAIN PAGE
# ==============================
# PAGE: Visualisasi 1
# ==============================
st.header("Visualisasi 1: Distribusi Jumlah Penyewaan Sepeda Berdasarkan Musim")
fig1 = px.box(data_day, x='season', y='cnt',
              labels={'cnt':'Jumlah Penyewaan Sepeda', 'season':'Musim'},
              category_orders={"season": ["1", "2", "3", "4"]})
fig1.update_traces(quartilemethod="inclusive")
fig1.update_xaxes(title_text='Musim')
fig1.update_yaxes(title_text='Jumlah Penyewaan Sepeda')
st.plotly_chart(fig1)

# PAGE: Visualisasi 2
# ==============================
st.header("Visualisasi 2: Perbedaan Pola Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan")
fig2 = px.box(data_day, x='workingday', y='cnt',
              labels={'cnt':'Jumlah Penyewaan Sepeda', 'workingday':'Tipe Hari'},
              category_orders={"workingday": ["0", "1"]})
fig2.update_xaxes(title_text='Tipe Hari', tickvals=[0, 1], ticktext=['Akhir Pekan', 'Hari Kerja'])
fig2.update_yaxes(title_text='Jumlah Penyewaan Sepeda')
st.plotly_chart(fig2)

# PAGE: Visualisasi 3
# ==============================
st.header("Visualisasi 3: Tren Penyewaan Sepeda Sepanjang Tahun untuk Pengguna Kasual dan Terdaftar")
fig3 = px.line(data_day, x='mnth', y=['casual', 'registered'],
               labels={'value':'Jumlah Penyewaan Sepeda', 'variable':'Tipe Pengguna', 'mnth':'Bulan'},
               category_orders={"mnth": list(range(1, 13))})
fig3.update_xaxes(title_text='Bulan', tickvals=list(range(1, 13)),
                  ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
fig3.update_yaxes(title_text='Jumlah Penyewaan Sepeda')
fig3.update_traces(mode='markers+lines')
st.plotly_chart(fig3)