import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from datetime import datetime

st.title("Sentimen Analisis dari cuitan pada Twitter mengenai Cacar Monyet")
st.markdown("Aplikasi ini digunakan untuk menganalisis sentimen dari 772 cuitan berbahasa Indonesia mengenai Cacar Monyet 💉🏥")

st.sidebar.title("Sentimen Analisis")
st.sidebar.markdown("Aplikasi ini digunakan untuk menganalisis sentimen dari 772 cuitan berbahasa Indonesia mengenai Cacar Monyet 💉🏥")

data_clean=pd.read_csv('df_copy_web.csv')

# st.markdown("""---""")
min_date = pd.to_datetime(data_clean['Datetime'].min(),format="%Y-%m-%d %H:%M:%S.%f")
max_date = pd.to_datetime(data_clean['Datetime'].max(),format="%Y-%m-%d %H:%M:%S.%f")
start_date, end_date = st.sidebar.date_input(label= 'Rentang Waktu',
                                                min_value =min_date,
                                                max_value =max_date,
                                                value=[min_date, max_date])
#-------------------------------------------

st.sidebar.subheader('Analisa Cuitan')
# tweets=st.sidebar.radio('Analisa berdasarkan tipe sentimen',('positive','negative'))
# st.markdown("#### Cuitan: ")
# st.write("1.  ", data_clean.query('label==@tweets')[['clean_text']].sample(1).iat[0,0])
# st.write("2.  ", data_clean.query('label==@tweets')[['clean_text']].sample(1).iat[0,0])
# st.write("3.  ", data_clean.query('label==@tweets')[['clean_text']].sample(1).iat[0,0])

if st.checkbox("Tampilkan 50 Data"):
     st.write(data_clean.head(50))

if st.checkbox("Tampilkan Hashtag"):
     from PIL import Image
     image = Image.open('hashtag.JPG')
     st.image(image, caption='Hashtag')

st.markdown("""---""")

data_clean['Datetime'] = pd.to_datetime(data_clean['Datetime'])
start_date = pd.to_datetime(start_date).tz_localize('UTC')
end_date = pd.to_datetime(end_date).tz_localize('UTC')

select_radio =st.sidebar.radio("Filter berdasarkan label", ["All","Positive", "Negative"], key=1)

if select_radio == 'Positive':
    outputs = data_clean[(data_clean['Datetime'] >= start_date) &
                        (data_clean['Datetime'] <= end_date) &
                        (data_clean['label'] == 'positive')]
elif select_radio == 'Negative':
    outputs = data_clean[(data_clean['Datetime'] >= start_date) &
                        (data_clean['Datetime'] <= end_date) &
                        (data_clean['label'] == 'negative')]
else:
    outputs = data_clean[(data_clean['Datetime'] >= start_date) &
                        (data_clean['Datetime'] <= end_date)]

if outputs.empty:
    st.write("Data tidak ditemukan")
else:
    if st.checkbox("Tampilkan Data Berdasarkan Label"):
        st.write(outputs.head(5))

#selectbox + visualisation
# An optional string to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content.
## Multiple widgets of the same type may not share the same key.


select=st.sidebar.selectbox('Visualisasi Cuitan',['Histogram','Pie Chart','Wordcloud'],key=2)
sentiment = outputs['label'].value_counts()
sentiment = pd.DataFrame({'Sentiment':sentiment.index, 'Tweets':sentiment.values})

if select == "Histogram":
        st.markdown("###  Histogram")
        fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
        st.plotly_chart(fig)
elif select == "Pie Chart":
        st.markdown("###  Pie Chart")
        fig = px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)
else:
        st.markdown("### Word Cloud")
        if select_radio == 'Positive':
                from PIL import Image
                image = Image.open('positive.png')
                st.image(image, caption='Positive Word Cloud')
        elif select_radio == 'Negative':
                from PIL import Image
                image = Image.open('negative.png')
                st.image(image, caption='Negative Word Cloud')
        else:
                from PIL import Image
                image = Image.open('all.png')
                st.image(image, caption='All Data')

        # if outputs == "positive":
        #         from PIL import Image
        #         image = Image.open('positive.png')
        #         st.image(image, caption='Positive Word Cloud')
        # elif outputs == "negative":
        #         from PIL import Image
        #         image = Image.open('negative.png')
        #         st.image(image, caption='Negative Word Cloud')
        # else:
        #         from PIL import Image
        #         image = Image.open('all.png')
        #         st.image(image, caption='All Data')

#        st.markdown("###  Word Cloud")
#        from PIL import Image
#        image = Image.open('WC_alltweets_MPOX_Indonesia_fix.png')
#        st.image(image, caption='Word Cloud Monkeypox')


# else:
#         st.markdown("###  Data Cuitan perbulan")
#         data_clean["Datetime"] = pd.to_datetime(data_clean["Datetime"], format="%Y-%m-%d %H:%M:%S.%f")
#         mask = (data_clean['Datetime'] > start_date) & (data_clean['Datetime'] <= end_date)
#         filtered_data = data_clean.loc[mask]
        
#         if select_radio != "All":
#                 filtered_data = filtered_data[filtered_data['label'] == label]
                
#         monthly_tweets = filtered_data.groupby([filtered_data["Datetime"].dt.year, filtered_data["Datetime"].dt.month]).count()
#         fig, ax = plt.subplots()
#         monthly_tweets.plot(kind='bar', x='Datetime', y='clean_text', ax=ax)
#         st.pyplot(fig)

        # monthly_tweets.plot(kind='bar', x='Datetime', y='clean_text')
        # st.pyplot()



# else:
#         st.markdown("###  Data Cuitan perbulan")
#         data_clean["Datetime"] = pd.to_datetime(data_clean["Datetime"], format="%Y-%m-%d %H:%M:%S.%f")
#         mask = (data_clean['Datetime'] > start_date) & (data_clean['Datetime'] <= end_date)
#         filtered_data = data_clean.loc[mask]
        
#         if select_radio != "All":
#                 filtered_data = filtered_data[filtered_data['label'] == label]
                
#         monthly_tweets = filtered_data.groupby([filtered_data["Datetime"].dt.year, filtered_data["Datetime"].dt.month]).count()
#         st.write(monthly_tweets)


# else: #x nya datetime y nya count
#         st.markdown("###  Data Cuitan perbulan")
#         # fig = px.bar()
#         data_clean["Datetime"] = pd.to_datetime(data_clean["Datetime"], format="%Y-%m-%d %H:%M:%S.%f")
#         months = data_clean.groupby(data_clean["Datetime"].dt.month).count().plot(kind="bar",legend=None, color='b',stacked=True)
#         months.set_xlabel("Bulan")
#         hist_months = months.get_figure()
#         st.pyplot(hist_months)



#------------------------------------------------------------------------
# select=st.sidebar.selectbox('Visualisasi Cuitan',['Histogram','Pie Chart','Wordcloud','Data Cuitan Perbulan'],key=2)
# select_radio =st.sidebar.radio("Filter by Label", ["Positive", "Negative"], key=1)

# if select_radio == 'Positive':
#     outputs = data_clean[(data_clean['Datetime'] >= start_date) &
#                         (data_clean['Datetime'] <= end_date) &
#                         (data_clean['label'] == 'positive')]
# elif select_radio == 'Negative':
#     outputs = data_clean[(data_clean['Datetime'] >= start_date) &
#                         (data_clean['Datetime'] <= end_date) &
#                         (data_clean['label'] == 'negative')]

# if outputs.empty:
#     st.write("Data tidak ditemukan")
# else:
#     sentiment=outputs['label'].value_counts()
#     sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})

#     if select == "Histogram":
#         st.markdown("###  Histogram")
#         fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
#         st.plotly_chart(fig)
#     elif select == "Pie Chart":
#         st.markdown("###  Pie Chart")
#         fig = px.pie(sentiment, values='Tweets', names='Sentiment')
#         st.plotly_chart(fig)
#     elif select == "Wordcloud":
#         st.markdown("###  Word Cloud")
#         from PIL import Image
#         image = Image.open('WC_alltweets_MPOX_Indonesia_fix.png')
#         st.image(image, caption='Word Cloud Monkeypox')
#     else: #x nya datetime y nya count
#         st.markdown("###  Data Cuitan perbulan")
#         # fig = px.bar()
#         data_clean["Datetime"] = pd.to_datetime(data_clean["Datetime"], format="%Y-%m-%d %H:%M:%S.%f")
#         months = outputs.groupby(outputs["Datetime"].dt.month).count().plot(kind="bar",legend=None, color='b',stacked=True)
#         months.set_xlabel("Bulan")
#         hist_months = months.get_figure()
#         st.pyplot(hist_months)


#------------------------------------------------------------------------

# data_clean['Datetime'] = pd.to_datetime(data_clean['Datetime'])
# start_date = pd.to_datetime(start_date).tz_localize('UTC')
# end_date = pd.to_datetime(end_date).tz_localize('UTC')

# select_radio =st.sidebar.radio("Filter by Label", ["Positive", "Negative"], key=1)
# select=st.sidebar.selectbox('Visualisasi Cuitan',['Histogram','Pie Chart','Wordcloud','Data Cuitan Perbulan'],key=2)

# if select_radio == 'Positive':
#     outputs = data_clean[(data_clean['Datetime'] >= start_date) &
#                         (data_clean['Datetime'] <= end_date) &
#                         (data_clean['label'] == 'positive')]
# elif select_radio == 'Negative':
#     outputs = data_clean[(data_clean['Datetime'] >= start_date) &
#                         (data_clean['Datetime'] <= end_date) &
#                         (data_clean['label'] == 'negative')]

# if outputs.empty:
#     st.write("Data tidak ditemukan")
# else:
#     sentiment=outputs['label'].value_counts()
#     sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})

#     if select == "Histogram":
#             st.markdown("###  Histogram")
#             fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
#             st.plotly_chart(fig)
#     elif select == "Pie Chart":
#             st.markdown("###  Pie Chart")
#             fig = px.pie(sentiment, values='Tweets', names='Sentiment')
#             st.plotly_chart(fig)
#     elif select == "Wordcloud":
#            st.markdown("###  Word Cloud")
#            from PIL import Image
#            image = Image.open('WC_alltweets_MPOX_Indonesia_fix.png')
#            st.image(image, caption='Word Cloud Monkeypox')
#     else: #x nya datetime y nya count
#             st.markdown("###  Data Cuitan perbulan")
#             # fig = px.bar()
#             outputs["Datetime"] = pd.to_datetime(outputs["Datetime"], format="%Y-%m-%d %H:%M:%S.%f")
#             months = outputs.groupby(outputs["Datetime"].dt.month).count().plot(kind="bar",legend=None, color='b',stacked=True)
#             months.set_xlabel("Bulan")
#             hist_months = months.get_figure()
#             st.pyplot(hist_months)



st.markdown("Data yang diolah merupakan data yang sudah dibersihkan, didapat dari cuitan pada Twitter sejak 08/01/2021 hingga 12/31/2022.")