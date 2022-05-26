import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_exercise_recommendationt() :
    st.title('연령별 운동 추천')
    # st.markdown("***") #라인줄
    image = Image.open('data/sub_main04_img.jpg')
    st.image(image, width=None, use_column_width=True)  
    st.markdown("***")
    df = pd.read_csv('data/gym_suggestion_ch.csv')
    st.dataframe(df, height=600)