from turtle import width
import streamlit as st
from PIL import Image
from app_by_item_gym import run_by_item_gym
from app_eda import run_eda
from app_exercise_recommendation import run_exercise_recommendationt
from app_gym_list import run_gym_list
from app_home import run_home
from app_ml import run_ml

import streamlit as st
st.set_page_config(layout="wide")
empty1,content1,empty3=st.columns([0.3,1.8,0.3])
with empty1:
        st.empty()

with empty3:
        st.empty()



with content1:
    def main() :
        
        image = Image.open('data/logo.png')
        st.sidebar.image(image)  
        
        menu = ['Home', '국내 체육관','종목별 체육관', '연령별 운동추천', 'EDA', 'ML']
        
        choice = st.sidebar.selectbox('main_menu', menu)

        if choice == menu[0] :
            run_home()
        elif choice == menu[1] :
            run_gym_list()
        elif choice == menu[2] : 
            run_by_item_gym()
        elif choice == menu[3] :
            run_exercise_recommendationt()
        elif choice == menu[0] :
            run_eda()
        elif choice == menu[1] :
            run_ml()

    if __name__ == '__main__' :
        main()