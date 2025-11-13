import pandas as pd
import plotly.express as px
import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta, date

st.title("Pertemuan 10: Streamlit dan Yahoo Finance")

 # ticker_symbol = 'GOOGL' ( baris ini dihaps saja karena sudah ada selectbox)
ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    ['GOOGL', 'MSFT', 'BBNI.JK', 'BMRI.JK']
)
ticker_data = yf.Ticker( 'GOOGL' )
# standar ISO untuk tanggal
# tgl_mulai = '2025-11-03' (diapus, pake string ajah u/ lebih interaktif)
tgl_mulai = str(
    st.date_input(
        'Tanggal mulai:',
        value = date.today()
    )
)
# tgl_akhir = '2025-11-07' (diapus, pake yg string ajah u/lebih interaktif)
tgl_akhir = str(
    st.date_input(
        'Tanggal akhir:',
        value = date.today()
    )
)
df = ticker_data.history(
    start=tgl_mulai,
    end=tgl_akhir
)
st.write(df.head())
st.write(df.tail())

grafik = px.line(
    df,
    y = ['Open','Close'],
    title = f'Harga saham {ticker_symbol}'
)
st.plotly_chart( grafik )
