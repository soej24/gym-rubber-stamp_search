from ast import Mult
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

from app_exercise_recommendation import run_exercise_recommendationt
from app_home import run_home
from app_serch import run_serch
from region_gym import run_region_gym

st.set_page_config(layout="wide")
sp1,con1,sp2=st.columns([0.2,1.2,0.2])
sp1,con2,con3,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con4,sp2 = st.columns([0.2,1.2,0.2])
sp1,con5,con6,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con7,sp2 = st.columns([0.2,1.2,0.2])



def main() :
    
    with sp1:
        st.empty()

    with con1:

        image = Image.open('data/logo.png')
        st.sidebar.image(image)  
        
        menu = ['Home', '체육관 검색','지역별 체육관 현황','지역별 국민의 체육관 참여도','연령별 운동추천']
        
        choice = st.sidebar.selectbox('main_menu', menu)

        if choice == menu[0] :
            run_home()

        elif choice == menu[1] :

            st.title('가까운 곳에서 체육관을 찾아보세요!!')

            st.markdown("***")
            image = Image.open('data/sub_main_img.jpg')
            st.image(image, width=None, use_column_width=True)  

            st.markdown("***")
          
            with con2 :

                df = pd.read_csv('data/gym_list_ch.csv')
                # st.dataframe(df)
                df_map = pd.read_csv('data/map02.csv', encoding='UTF-8')
                # st.dataframe(df_map)

                addr_1 = ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','울산광역시','세종특별자치시','경기도','강원도',\
                            '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치제도']
                column_list = ['태권도','합기도', '주짓수', '유도', '공수도', '킥복싱', '복싱', '택견', '검도', '마샬아츠', '트릭킹','멀티']
                choice_list = st.selectbox('지역을 선택하세요!', addr_1, index=3)

                addr_3 = st.text_input('읍면동을 입력하세요! ex)구월동', max_chars=20)

            with con3 :

                addr_2 = st.text_input('시/군을 입력하세요! ex)강남구, 창원시 성산구', max_chars=20)
                choice_list2 = st.selectbox('운동 종목을 선택하세요! (종목이 없는 체육관은 멀티로 분류)', column_list, index=0)

            with con4 :

                if st.button('검색') :
                    #st.text(choice_list2)

                    if choice_list2 == '멀티' :
                        # choice_list2 = df[ ~df['사업장명'].str.contains('태권도') & ~df['사업장명'].str.contains('합기도') & ~df['사업장명'].str.contains('주짓수') & \
                        # ~df['사업장명'].str.contains('복싱') & ~df['사업장명'].str.contains('택견') & ~df['사업장명'].str.contains('검도') & \
                        # ~df['사업장명'].str.contains('마샬아츠') & ~df['사업장명'].str.contains('택견')]

                        df_mlt = df[ (df['소재지전체주소'].str.contains('인천광역시')) & (df['소재지전체주소'].str.contains('남동구')) & \
                            (df['소재지전체주소'].str.contains('구월동')) & (~df['사업장명'].str.contains('태권도') & \
                             ~df['사업장명'].str.contains('합기도') & ~df['사업장명'].str.contains('주짓수') & ~df['사업장명'].str.contains('복싱') & \
                             ~df['사업장명'].str.contains('택견') & ~df['사업장명'].str.contains('검도') & ~df['사업장명'].str.contains('마샬아츠') & \
                             ~df['사업장명'].str.contains('택견'))]
                        st.table(df_mlt)

                    else :
                        
                        df = df[ (df['소재지전체주소'].str.contains(choice_list)) & (df['소재지전체주소'].str.contains(addr_2)) &\
                                    (df['소재지전체주소'].str.contains(addr_3)) & (df['사업장명'].str.contains(choice_list2))]
                        df = df.reset_index(drop=True)                  
                        
                        if df.empty :
                            st.markdown("***")                            
                            st.text('검색된 데이터가 없습니다!!')
                        else : 
                            st.table(df)

                            st.markdown("***")
                            # new_df_map = df_map[ (df_map['시도'] == '인천광역시') & (df_map['시군구'] == '남동구') & (df_map['읍면동'] == '구월동') ]
                            new_df_map = df_map[ (df_map['시도'] == choice_list) & (df_map['시군구'] == addr_2) & (df_map['읍면동'] == addr_3) ]
                            st.map(new_df_map)

        elif choice == menu[2] :
            run_region_gym()        

        elif choice == menu[3] :

            st.title('지역별 국민의 체육관 참여도')

            st.markdown("***")    
            image = Image.open('data/sub_main03_img.jpg')
            st.image(image, width=None, use_column_width=True) 
            st.markdown("***")           

            df = pd.read_csv('data/gym_use.csv',  encoding='UTF-8')                
            
            with con5 :
                st.markdown("""
                                <style>
                                .css-1d391kg {
                                    padding-top: 3.5rem;
                                padding-right: 1rem;
                                padding-bottom: 3.5rem;
                                padding-left: 1rem;}
                                </style>
                                """, unsafe_allow_html=True)         

                    
                st.subheader('┏ 지역별 참여 리스트 ┓')
                df_groupby = df.groupby('시도명')['인구수'].count().sort_values(ascending = False)
                st.table(df_groupby)

            with con6 :

                st.subheader('┏ 파이 차트 보기 ┓')
                fig1 =  px.pie(df, names='시도명', values='인구수')
                st.plotly_chart(fig1)


            with con7 :     

                df_chart = df['시도명'].value_counts()
                st.line_chart(df_chart)

        elif choice == menu[4] :
            run_exercise_recommendationt()
    with sp2:
        st.empty()


if __name__ == '__main__' :
    main()