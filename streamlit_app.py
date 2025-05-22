import streamlit as st

st.title("🔥Nandoss🔥")
st.write(
    "focus on your goals"
)
st.image("View/IMG_4111.jpeg")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
    
