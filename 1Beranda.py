import streamlit as st
import streamlit as st
from googletrans import Translator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

st.write("# Selamat Datang di Web App Analisis Sentimen Linear SVM! 👋")

st.markdown(
    """
    *Web Application* ini merupakan *sentiment analyzer* yang dibuat menggunakan model
    machine learning dengan metode *Linear Support Vector Machine* yang
    memiliki akurasi sebesar 91%. *Sentiment analyzer* ini memberikan output 
    berupa tiga kelas sentimen yaitu **positif✔️, netral➖,** atau **negatif❌**.
"""
)

st.sidebar.success("Menu Sidebar 👆")

#---------------------------------------#

#Read data
data = pd.read_excel('label diagram lingkaran 2.xlsx')
df=pd.DataFrame(data)

#Split data training dan testing
y=df.score.values
x=df.english.values
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify = y, random_state=1,
                                    test_size=0.2, shuffle=True)

#CountVectorizer dan N-Gram
vectorizer = CountVectorizer(analyzer = 'word', ngram_range=(1,1), binary=True, stop_words='english')
vectorizer.fit (list(x_train) + list(x_test))
x_train_vec = vectorizer.transform(x_train)
x_test_vec = vectorizer.transform(x_test)

#Membuat Classifier SVM Linear
linear = svm.SVC(kernel='linear', C=1)
linear.fit(x_train_vec, y_train).predict(x_test_vec)

# Input teks
translator = Translator()
message = st.text_area("Ketik teks di bawah ini 👇")

# Fungsi untuk memeriksa apakah teks memiliki minimal 3 kata
def is_valid_input(text):
    return len(text.split()) >= 3

# Klasifikasi
if st.button("Klasifikasi sentimen teks"):
    if is_valid_input(message):
        try:
            translated_text = translator.translate(message, src='id', dest='en').text
            text_vector = vectorizer.transform([translated_text])
            sentiment = linear.predict(text_vector)
            st.success(f"Sentimen: {sentiment[0]}")
        except TypeError:
            st.error("Terjadi kesalahan saat menerjemahkan atau mengklasifikasikan teks.")
    else:
        st.error("Harap masukkan teks dengan minimal 3 kata.")