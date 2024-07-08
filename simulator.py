import streamlit as st
from streamlit_option_menu import option_menu                      

with st.sidebar : 
    selected = option_menu ('Mengitung Volume Bangun Ruang',
                            ['Hitung Volume Balok',
                             'Hitung Volume Tabung'],
                             default_index=0)

if (selected == 'Hitung Volume Balok') : 
    st.title('Hitung Volume Balok')
    panjang = st.slider ("masukan nilai panjang",0.0,100.0)
    lebar = st.slider ("masukan nilai lebar",0.0,100.0)
    tinggi = st.slider ("masukan nilai tinggi",0.0,100.0)
    hitung = st.button ("hitung volume")

    if hitung : 
        volume = panjang * lebar * tinggi
        st.success (f"volume Balok adalah = {volume}")

if (selected == 'Hitung Volume Tabung') : 
    st.title('Menghitung Volume Tabung')
    r = st.slider ("masukan nilai jari-jari",0.0,100.0)
    tinggi = st.slider ("masukan nilai tinggi",0.0,100.0)
    hitung = st.button ("hitung volume")
    phi = 3.14
    if hitung : 
        volume = phi * r * r * tinggi
        st.success (f"volume Tabung adalah = {volume}")
        