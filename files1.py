import streamlit as st
import pandas as pd

st.subheader('Uploading the CSV file.')
# this is to upload the file
df=st.file_uploader('Upload the CSV file : ', type=['csv','xslx'])
st.subheader('Loading the CSV file')
# this is to show the uploaded file datas in data frame in the website only
if df is not None:
    df=pd.read_csv(df)
    st.table(df.head(10))


st.subheader('Dealing with images')
img=st.file_uploader('Upload the Image file : ', type=['png','jpeg','jpg'])
if img is not None:
    img=st.image(img)


st.subheader('Working with videos')
video=st.file_uploader('Upload the Video file : ', type=['mp4','mkv'])
if video is not None:
    video=st.video(video)

st.subheader('Working with Audio')
audio=st.file_uploader('Upload the Audio file : ', type=['mp3','wav'])
if audio is not None:
    audio=st.audio(audio)