import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from datetime import datetime

st.title("Sentimen Analisis dari cuitan pada Twitter mengenai Monkeypox")
st.markdown("Aplikasi ini digunakan untuk menganalisis sentimen dari 15000+ cuitan berbahasa Indonesia mengenai Monkeypox 🐵")

st.sidebar.title("Sentimen Analisis")
st.sidebar.markdown("Aplikasi ini digunakan untuk menganalisis sentimen dari 15000+ cuitan berbahasa Indonesia mengenai Monkeypox 🐵")

data=pd.read_csv('tweet_data_TweetMPOXfixclean (4).csv')


st.sidebar.subheader('Analisa Cuitan')
tweets=st.sidebar.radio('Analisa berdasarkan tipe sentimen',('positive','negative','neutral'))
st.markdown("#### Cuitan: ")
st.write("1.  ", data.query('label==@tweets')[['Text']].sample(1).iat[0,0])
st.write("2.  ", data.query('label==@tweets')[['Text']].sample(1).iat[0,0])
st.write("3.  ", data.query('label==@tweets')[['Text']].sample(1).iat[0,0])

if st.checkbox("Tampilkan 50 Data"):
    st.write(data.head(50))

st.markdown("""---""")

st.markdown("#### Perbandingan antar cuitan: ")
st.write(data.query('label==@tweets')[['Text', 'clean_text','label']].head())

st.markdown("""---""")

#selectbox + visualisation
# An optional string to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content.
## Multiple widgets of the same type may not share the same key.
select=st.sidebar.selectbox('Visualisasi Cuitan',['Histogram','Pie Chart','Wordcloud', 'Data Cuitan Perbulan'],key=1)
sentiment=data['label'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})

if select == "Histogram":
        st.markdown("###  Histogram")
        fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
        st.plotly_chart(fig)
elif select == "Pie Chart":
        st.markdown("###  Pie Chart")
        fig = px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)
elif select == "Wordcloud":
       st.markdown("###  Word Cloud")
       from PIL import Image
       image = Image.open('WC_alltweets_MPOX_Indonesia(2).png')
       st.image(image, caption='Word Cloud Monkeypox')
else: #x nya datetime y nya count
        st.markdown("###  Data Cuitan perbulan")
        # fig = px.bar()
        data["Datetime"] = pd.to_datetime(data["Datetime"], format="%Y-%m-%d %H:%M:%S.%f")
        months = data.groupby(data["Datetime"].dt.month).count().plot(kind="bar",legend=None, color='b',stacked=True)
        months.set_xlabel("Bulan")
        hist_months = months.get_figure()
        st.pyplot(hist_months)


st.markdown("Data yang diolah merupakan data yang didapat dari cuitan Twitter sejak 07/28/2022 hingga 12/31/2022.")