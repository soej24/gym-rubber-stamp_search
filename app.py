import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

def main() :
    st.title('우리집에서 가까운 체육관 찾기')

    menu = ['Home', '국내 체육관','종목별 체육관', '연령별 운동추천', 'EDA', 'ML']

    st.sidebar.selectbox('', menu)


if __name__ == '__main__' :
    main()