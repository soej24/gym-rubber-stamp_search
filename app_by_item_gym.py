import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_by_item_gym() :

    st.title('종목별 체육관 검색')
    image = Image.open('data/sub_main03_img.jpg')
    st.image(image, width=None, use_column_width=True)         
    st.markdown("***")
    df = pd.read_csv('data/gym_list_ch.csv')
    #st.dataframe(df)

    column_list = ['태권도','합기도', '주짓수', '유도', '공수도', '킥복싱', '복싱', '택견', '검도', '마샬아츠', '트릭킹']
    choice_list = st.selectbox('운동 종목을 선택하세요!', column_list, index=0)

    if choice_list == column_list[0] :
        st.dataframe(df[ df['사업장명'].str.contains('태권도')], height=500)
    elif choice_list == column_list[1]:
        st.dataframe(df[ df['사업장명'].str.contains('합기도')])
    elif choice_list == column_list[2]:
        st.dataframe(df[ df['사업장명'].str.contains('주짓수')])
    elif choice_list == column_list[3]:
        st.dataframe(df[ df['사업장명'].str.contains('유도')])
    elif choice_list == column_list[4]:
        st.dataframe(df[ df['사업장명'].str.contains('공수도')])     
    elif choice_list == column_list[5]:
        st.dataframe(df[ df['사업장명'].str.contains('킥복싱')])
    elif choice_list == column_list[6]:
        st.dataframe(df[ df['사업장명'].str.contains('복싱')])
    elif choice_list == column_list[7]:
        st.dataframe(df[ df['사업장명'].str.contains('택견')])   
    elif choice_list == column_list[8]:
        st.dataframe(df[ df['사업장명'].str.contains('검도')])               
    elif choice_list == column_list[9]:
        st.dataframe(df[ df['사업장명'].str.contains('마샬아츠')])
    elif choice_list == column_list[10]:
        st.dataframe(df[ df['사업장명'].str.contains('트릭킹')])