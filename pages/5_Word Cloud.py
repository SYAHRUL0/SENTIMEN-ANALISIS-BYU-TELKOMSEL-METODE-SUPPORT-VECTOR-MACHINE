import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Word Cloud")

st.title("Sebaran Word Cloud Tweet Netral ,Negatif ,Positif")
images = ['wrcld netral.PNG', 'wrdcld negatif.PNG','wrdcld positif.PNG']
st.image(images, width=150 * len(images))
st.markdown(
    """
    Dengan menggunakan Word Cloud, bisa diketahui sebaran
    sentimen data tweeet. frekuensi kata-kata dapat di
    tampilkan dalam bentuk menarik dan juga informatif

    """
)