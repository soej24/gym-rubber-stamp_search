import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#importing required libraries

def run_home() :
    st.title('우리집에서 가까운 체육관 찾기')
    image = Image.open('data/img05.jpg')
    st.image(image, width=None, use_column_width=True)  
    st.markdown("***")
    
    df = pd.read_csv('data/gym_list_ch.csv')
    # st.dataframe(df)

    addr_1 = ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','울산광역시','세종특별자치시','경기도','강원도',\
                '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치제도']

    choice_list = st.selectbox('지역을 선택하세요!', addr_1, index=0)
    addr_2 = st.text_input('시/군을 입력하세요! ex)강남구, 창원시 성산구', max_chars=20)
    addr_3 = st.text_input('동을 입력하세요! ex)구월동', max_chars=20)
    column_list = ['태권도','합기도', '주짓수', '유도', '공수도', '킥복싱', '복싱', '택견', '검도', '마샬아츠', '트릭킹','멀티']
    choice_list2 = st.selectbox('운동 종목을 선택하세요!', column_list, index=0)

    if choice_list2 == '멀티' :
        choice_list2 = st.dataframe(df[ ~df['사업장명'].str.contains('태권도') & ~df['사업장명'].str.contains('합기도') & ~df['사업장명'].str.contains('주짓수') & \
        ~df['사업장명'].str.contains('복싱') & ~df['사업장명'].str.contains('택견') & ~df['사업장명'].str.contains('검도') & \
        ~df['사업장명'].str.contains('마샬아츠') & ~df['사업장명'].str.contains('택견')], height=500)



    # df[ (df['소재지전체주소'].str.contains('경기도')) & (df['소재지전체주소'].str.contains('성남시')) & (df['소재지전체주소'].str.contains('중앙동')) ] 

    if st.button('검색') :
        # st.subheader(choice_list1)
        # st.subheader(addr_2)
        # st.subheader(addr_3)
        # st.subheader(choice_list2)
        df = df[ (df['소재지전체주소'].str.contains(choice_list)) & (df['소재지전체주소'].str.contains(addr_2)) &\
                 (df['소재지전체주소'].str.contains(addr_3)) & (df['사업장명'].str.contains(choice_list2))]
        df = df.reset_index(drop=True)
        # st.dataframe(df, height=500)
        st.table(df)
    st.markdown("***")
    st.title('지도 들어갈 부분')

    df_map = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])