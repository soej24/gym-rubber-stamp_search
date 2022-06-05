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
sp1,con4,sp2=st.columns([0.2,1.2,0.2])



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
            run_serch()

        elif choice == menu[2] :
            run_region_gym()        

        elif choice == menu[3] :
            st.title('지역별 국민의 체육관 참여도')

            st.markdown("***")    
            image = Image.open('data/sub_main03_img.jpg')
            st.image(image, width=None, use_column_width=True) 
            st.markdown("***")           

            df = pd.read_csv('data/gym_use.csv',  encoding='UTF-8')                
            
            with con2 :
                st.markdown("""
                                <style>
                                .css-1d391kg {
                                padding-top: 3.5rem;
                                padding-right: 1rem;
                                padding-bottom: 3.5rem;
                                padding-left: 1rem;}
                                </style>
                                """, unsafe_allow_html=True)       
                    
                st.subheader('지역별 참여 리스트')
                df_groupby = df.groupby('시도명')['인구수'].count().sort_values(ascending = False)
                st.table(df_groupby)

            with con3 :
                st.markdown("""
                                <style>
                                .css-1d391kg {
                                padding-top: 3.5rem;
                                padding-right: 1rem;
                                padding-bottom: 3.5rem;
                                padding-left: 1rem;}
                                </style>
                                """, unsafe_allow_html=True)  
                fig1 =  px.pie(df, names='시도명', values='인구수')
                st.plotly_chart(fig1)

            with con4 :
                st.markdown("***")    
                df_chart = df['시도명'].value_counts()
                st.line_chart(df_chart)

        elif choice == menu[4] :
            run_exercise_recommendationt()
    with sp2:
        st.empty()


if __name__ == '__main__' :
    main()