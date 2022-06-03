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
    image = Image.open('data/img05.jpg')
    st.image(image, width=None, use_column_width=True)  

    st.markdown("***")

    df = pd.read_csv('data/gym_list_ch.csv')
    #df.loc[ df.groupby('소재지전체주소')['소재지전체주소'].count().sort_values(ascending = False), ]

    # if choice_list == addr_1[] :
    #     addr_2 = []
    #     choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    addr_1 = ['서울특별시','인천광역시','대전광역시','광주광역시','대구광역시','부산광역시','울산광역시','세종특별자치시','제주특별자치도','강원도',\
            '경기도', '경상남도', '경상북도', '전라남도', '전라북도', '충청남도', '충청북도']
    choice_list = st.selectbox('지역을 선택하세요!', addr_1)

    if choice_list == addr_1[0] :
        addr_2 = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구',\
                  '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구',\
                  '중랑구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)

    if choice_list == addr_1[1] :
        addr_2 = ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)

    if choice_list == addr_1[2] :
        addr_2 = ['대덕구', '동구', '서구', '유성구', '중구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)       

    if choice_list == addr_1[3] :
        addr_2 = ['광산구', '남구', '동구', '북구', '서구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)        

    if choice_list == addr_1[4] :
        addr_2 = ['남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[5] :
        addr_2 = ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구',\
                  '중구', '해운대구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[6] :
        addr_2 = ['남구', '동구', '북구', '울주군', '중구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[7] :
        addr_2 = ['세종특별자치시']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[8] :
        addr_2 = ['서귀포시', '제주시']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[9] :
        addr_2 = ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군',\
                  '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[10] :
        addr_2 = ['가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시', '구리시', '군포시',\
                  '김포시', '남양주시', '동두천시', '부천시', '성남시', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시',\
                  '수원시 권선구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '시흥시', '안산시', '안산시 단원구', '안산시',\
                  '상록구', '안성시', '안양시', '안양시 동안구', '안양시 만안구', '양주시', '양평군', '여주시', '연천군', '오산시',\
                  '용인시', '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시', '이천시', '파주시', '평택시',\
                  '포천시', '하남시', '화성시']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[11] :
        addr_2 = ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군',\
                  '창원시',' 창원시 마산합포구', '창원시 마산회원구', '창원시 성산구', '창원시 의창구', '창원시 진해구', '통영시', '하동군',\
                  '함안군', '함양군', '합천군']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[12] :
        addr_2 = ['경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군',\
                  '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시', '포항시 남구',\
                  '포항시 북구']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[13] :
        addr_2 = ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군', '순천시', '신안군',\
                  '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[14] :
        addr_2 = ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시 덕진구',\
                  '전주시 완산구', '정읍시', '진안군']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[15] :
        addr_2 = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '연기군', '예산군', '천안시',\
                  '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    if choice_list == addr_1[16] :
        addr_2 = ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청원군', '청주시 상당구', '청주시 서원구',\
                  '청주시 청원구', '청주시 흥덕구', '충주시']
        choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

    addr_3 = st.text_input('읍면동을 입력하세요! ex)구월동', max_chars=20)

    column_list = ['태권도','합기도', '주짓수', '유도', '공수도', '킥복싱', '복싱', '택견', '검도', '마샬아츠', '트릭킹','멀티']
    gym_list = st.selectbox('운동 종목을 선택하세요! (종목이 없는 체육관은 멀티로 분류)', column_list, index=0) 
 
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
                        
    df = df[ (df['소재지전체주소'].str.contains(choice_list)) & (df['소재지전체주소'].str.contains(choice_list2)) &\
                (df['소재지전체주소'].str.contains(addr_3)) & (df['사업장명'].str.contains(gym_list))]

    st.markdown("""
                    <style>
                    .css-1d391kg {
                        padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;}
                    </style>
                    """, unsafe_allow_html=True)    
                    
    st.dataframe(df)
    st.markdown("***") 


