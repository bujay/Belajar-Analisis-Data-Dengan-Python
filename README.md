# Belajar-Analisis-Data-Dengan-Python

# Analisis Data Penyewaan Sepeda

## Ikhtisar
Proyek ini menyediakan analisis mendalam mengenai dataset penyewaan sepeda. Analisis bertujuan untuk mengungkap pola-pola dalam penyewaan sepeda lintas musim, perbandingan hari kerja dengan akhir pekan, serta jenis pengguna. Repositori ini meliputi notebook analisis serta dashboard Streamlit untuk eksplorasi data interaktif.

## Penulis
- **Nama:** Ahmad Bujai Rimi
- **Email:** [ahmadbujai20@gmail.com](mailto:ahmadbujai20@gmail.com)
- **MyProfil Dicoding:** [Dicoding Indonesia](https://www.dicoding.com/users/bujai_rimi/academies)

## Berkas
- `Proyek_Analisis_Data.ipynb`: Notebook Jupyter yang berisi analisis data.
- `dashboard/`: Direktori yang berisi aplikasi dashboard Streamlit.

## Temuan Kunci
- **Tren Musiman**: Analisis menunjukkan bahwa musim panas mengalami jumlah penyewaan sepeda tertinggi, yang menandakan popularitasnya karena kondisi cuaca yang mendukung.
- **Perbandingan Hari Kerja vs Akhir Pekan**: Terdapat median penyewaan sepeda yang sedikit lebih tinggi pada hari kerja, tetapi akhir pekan menunjukkan variasi yang lebih besar, menandakan adanya fluktuasi dalam penyewaan.
- **Tren Tahunan**: Pengguna terdaftar secara konsisten menyewa lebih banyak sepeda sepanjang tahun, dengan peningkatan yang signifikan pada pengguna kasual selama bulan-bulan musim panas.

## Cara Menjalankan
- Notebook Jupyter dapat dilihat langsung di GitHub atau dijalankan dalam lingkungan yang mendukung Jupyter Notebook Python.
- Dashboard Streamlit dapat dijalankan secara lokal dengan navigasi ke direktori `dashboard/` dan menjalankan `streamlit run dashboard.py`.

## Dashboard
Dashboard Streamlit mencakup fitur-fitur berikut:
- Tampilan interaktif dari data mentah dan statistik ringkasan.
- Visualisasi yang menjawab pertanyaan bisnis kunci.
- Analisis komparatif penyewaan sepeda pada hari kerja dan akhir pekan.
- Analisis tren penyewaan sepeda sepanjang tahun.

## Kebutuhan dan Instalasi

Proyek ini memerlukan pustaka-pustaka berikut untuk berjalan dengan baik:

- Matplotlib 3.8.3
- NumPy 1.26.4
- Pandas 2.2.0
- Plotly 5.19.0
- Seaborn 0.13.2
- Streamlit 1.31.1

Kamu dapat menginstal semua pustaka yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:

```bash
pip install matplotlib numpy pandas plotly seaborn streamlit
