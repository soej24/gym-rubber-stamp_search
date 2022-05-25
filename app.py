import streamlit as st

def main() :
    st.title('우리집에서 가까운 체육관 찾기')

    menu = ['Home', '국내 체육관','종목별 체육관', '연령별 운동추천']
    menu2 = ['EDA', 'ML']
    st.sidebar.selectbox('', menu)
    st.sidebar.selectbox('', menu2)

    input = st.text_input("message")
    st.write(input)

if __name__ == '__main__' :
    main()