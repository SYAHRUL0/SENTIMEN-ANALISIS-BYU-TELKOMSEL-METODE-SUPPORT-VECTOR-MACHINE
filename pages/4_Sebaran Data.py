import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Sebaran Data")

st.title("Sebaran Sentimen Data Tweet")
images = ['bar_svm.png', 'pie chart svm benar.png']
st.image(images, width=150 * len(images))
st.markdown(
    """
    Dengan menggunakan bar chart dan pie chart, bisa diketahui sebaran
    sentimen data tweeet . Data sentimen positif memiliki jumlah 
    yaitu 1037 data. Data sentiment negatif memiliki jumlah
    yaitu berjumlah 625 data. Data sentimen netral
    memiliki jumlah yaitu 1205 data.

    """
)