from re import L
from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from app_eda import run_eda
from app_exercise_recommendation import run_exercise_recommendationt
from app_home import run_home
from app_ml import run_ml
from app_serch import run_serch

st.set_page_config(layout="wide")
empty1,content1,empty3=st.columns([0.1,1.2,0.1])
empty4,col1,col2,empty5 = st.columns(4)


def main() :
    
    with empty1:
        st.empty()

    with content1:

        image = Image.open('data/logo.png')
        st.sidebar.image(image)  
        
        menu = ['Home', '체육관 검색','연령별 운동추천', '지역별 국민의 체육관 참여운동', 'ML']
        
        choice = st.sidebar.selectbox('main_menu', menu)

        if choice == menu[0] :
            run_home()
        elif choice == menu[1] :
            run_serch()        
        elif choice == menu[2] :
            run_exercise_recommendationt()
        elif choice == menu[3] :

            st.title('지역별 국민의 체육관 참여운동')

            st.markdown("***")    
            image = Image.open('data/sub_main03_img.jpg')
            st.image(image, width=None, use_column_width=True) 
            st.markdown("***") 
            
            with empty4 :
                st.empty()
            with col1 : 
                df = pd.read_csv('data/gym_use.csv',  encoding='UTF-8')
                st.dataframe(df)
            with col2 :
                st.dataframe(df)
            with empty5 :
                st.empty()
            
                #run_eda()
        
        elif choice == menu[4] :
            run_ml()

    with empty3:
        st.empty()

if __name__ == '__main__' :
    main()