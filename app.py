import streamlit as st
from PIL import Image

def main() :
    image = Image.open('data/logo.png')
    st.sidebar.image(image)  
    
    st.title('우리집에서 가까운 체육관 찾기')

    menu = ['Home', '국내 체육관','종목별 체육관', '연령별 운동추천']
    menu2 = ['EDA', 'ML']



    
    st.sidebar.selectbox('main_menu', menu)
    st.sidebar.selectbox('EDA', menu2)


if __name__ == '__main__' :
    main()