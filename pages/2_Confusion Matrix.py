import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Confusion Matrix")

st.title("Confusion Matrix")
image = Image.open('confusionmatrix_svm.png')
st.image(image, width = 400)
st.markdown(
    """
    - 108 data negatif yang teridentifikasi dengan 
      benar bersentimen negatif, 
      12 data negatif teridentifikasi netral, 
      dan 5 data negatif teridentifikasi positif.
    - 236 data netral benar teridentifikasi dengan benar 
      bersentimen netral, 0 data netral teridentifikasi 
      negatif, dan 5 data netral teridentifikasi positif.
    - 178 data positif teridentifikasi dengan benar 
      bersentimen positif, 7 data positif teridentifikasi 
      negatif, dan 23 data positif teridentifikasi netral.
"""
)