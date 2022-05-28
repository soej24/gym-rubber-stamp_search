import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


def run_eda() :
    st.title('지역별 국민의 체육관 참여운동')

    st.markdown("***")    
    image = Image.open('data/sub_main03_img.jpg')
    st.image(image, width=None, use_column_width=True)  
    df = pd.read_csv('data/gym_use.csv',  encoding='UTF-8')
    st.dataframe(df, width=520)

    st.subheader('지역별 체육관 분포 차트')
    st.subheader('연령에 따른 운동여부 상관관계연령에 따른 운동여부 상관관계연령에 따른 운동여부 상관관계연령에 따른 운동여부 상관관계연령에 따른 운동여부 상관관계연령에 따른 운동여부 상관관계')