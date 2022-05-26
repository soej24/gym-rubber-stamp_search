import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_gym_list() :
    st.title('국내 체육관 리스트')
    # st.markdown("***") #라인줄
    image = Image.open('data/sub_main_img.jpg')
    st.image(image, width=None, use_column_width=True)  
    st.markdown("***")
    df = pd.read_csv('data/gym_list_ch.csv')
    st.dataframe(df, height=600)

    df['성별'].str.replace('M','남자')
    st.dataframe(df)