from pyrsistent import v
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



def run_region_gym() :

    st.title('지역별 체육관 현황!!')

    st.markdown("***")
    image = Image.open('data/img06.jpg')
    st.image(image, width=None, use_column_width=True)  

    st.markdown("***")
    st.markdown("""
                <style>
                .css-1d391kg {
                    padding-top: 3.5rem;
                padding-right: 1rem;
                padding-bottom: 3.5rem;
                padding-left: 1rem;}
                </style>
                """, unsafe_allow_html=True)         
    df = pd.read_csv('data/gym_list_ch.csv')
    df.loc[ df.groupby('소재지전체주소')['소재지전체주소'].count().sort_values(ascending = False), ]
    # st.subheader('┏ 전체 체육관 ┓')    
    # st.dataframe(df, height=500) 

    my_order = ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','울산광역시','세종특별자치시','경기도','강원도',\
                '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치제도']
    status = st.radio('지역을 선택하세요!', my_order)
    # df.loc[ df['소재지전체주소'].str.contains('경기도'), ]
    df = df.loc[ df['소재지전체주소'].str.contains(status), ]
    st.markdown("***") 

    # 첫번째 방법
    if status == my_order[0] :        
        st.table(df.sort_values('소재지전체주소'))
    elif status == my_order[1] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[2] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[3] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[4] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[5] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[6] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[7] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[8] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[9] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[10] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[11] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[12] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[13] :
        st.dataframe(df.sort_values('소재지전체주소'))
    elif status == my_order[14] :
        st.dataframe(df.sort_values('소재지전체주소'))
