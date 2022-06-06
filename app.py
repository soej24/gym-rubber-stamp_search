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
sp1,con4,con5,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con6,con7,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con8,con9,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con10,con11,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con12,con13,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con14,con15,sp2 = st.columns([0.2,0.6,0.6,0.2])
sp1,con16,con17,sp2 = st.columns([0.2,0.6,0.6,0.2])


def main() :
    
    with sp1:
        st.empty()

    with con1:
        image = Image.open('data/logo.png')
        st.sidebar.image(image)  
        
        menu = ['Home', '체육관 검색','지역별 체육관 현황','지역별 체육도장 동호회 현황','연령별 운동추천']        
        choice = st.sidebar.selectbox('main_menu', menu)

        if choice == menu[0] :
            run_home()

        elif choice == menu[1] :
            run_serch()

        elif choice == menu[2] :
            run_region_gym()        

        elif choice == menu[3] :
            st.title('지역별 체육도장 동호회 현황')

            st.markdown("***")    
            image = Image.open('data/sub_main03_img.jpg')
            st.image(image, width=None, use_column_width=True) 
            st.markdown("***")           

            gym_use = pd.read_csv('data/gym_use_last.csv',  encoding='UTF-8')               

            st.markdown("""
                            <style>
                            .css-1d391kg {
                            padding-top: 3.5rem;
                            padding-right: 1rem;
                            padding-bottom: 3.5rem;
                            padding-left: 1rem;}
                            </style>
                            """, unsafe_allow_html=True)      

            with con2 :
                # 서울특별시
                gym_use_total1 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['서울특별시']
                st.subheader('서울특별시')
                st.table(gym_use_total1)

                gym_use_1 = gym_use.loc[ gym_use['시도명'].str.contains('서울특별시'), ]
                gym_use_1.groupby('군구명')['회원수'].sum()

                fig1 =  px.pie(gym_use_1, names='군구명', values='회원수')
                st.plotly_chart(fig1)

            with con3 :
                # 인천광역시
                gym_use_total2 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['인천광역시']
                st.subheader('인천광역시')
                st.table(gym_use_total2)     

                gym_use_2 = gym_use.loc[ gym_use['시도명'].str.contains('인천광역시'), ]
                gym_use_2.groupby('군구명')['회원수'].sum()

                fig2 =  px.pie(gym_use_2, names='군구명', values='회원수')
                st.plotly_chart(fig2)

            with con4 :
                # 대전광역시
                gym_use_total3 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['대전광역시']
                st.subheader('대전광역시')
                st.table(gym_use_total3)  

                gym_use_3 = gym_use.loc[ gym_use['시도명'].str.contains('대전광역시'), ]
                gym_use_3.groupby('군구명')['회원수'].sum()

                fig3 =  px.pie(gym_use_3, names='군구명', values='회원수')
                st.plotly_chart(fig3)

            with con5 :
                # 광주광역시
                gym_use_total4 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['광주광역시']
                st.subheader('광주광역시')
                st.table(gym_use_total4)   

                gym_use_4 = gym_use.loc[ gym_use['시도명'].str.contains('광주광역시'), ]
                gym_use_4.groupby('군구명')['회원수'].sum()

                fig4 =  px.pie(gym_use_4, names='군구명', values='회원수')
                st.plotly_chart(fig4)

            with con6 :
                # 대구광역시
                gym_use_total5 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['대구광역시']
                st.subheader('대구광역시')
                st.table(gym_use_total5)          

                gym_use_5 = gym_use.loc[ gym_use['시도명'].str.contains('대구광역시'), ]
                gym_use_5.groupby('군구명')['회원수'].sum()

                fig5 =  px.pie(gym_use_5, names='군구명', values='회원수')
                st.plotly_chart(fig5)

            with con7 :
                # 부산광역시
                gym_use_total6 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['부산광역시']
                st.subheader('부산광역시')
                st.table(gym_use_total6)  

                gym_use_6 = gym_use.loc[ gym_use['시도명'].str.contains('부산광역시'), ]
                gym_use_6.groupby('군구명')['회원수'].sum()

                fig6 =  px.pie(gym_use_6, names='군구명', values='회원수')
                st.plotly_chart(fig6)

            with con8 :
                # 울산광역시
                gym_use_total7 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['울산광역시']
                st.subheader('울산광역시')
                st.table(gym_use_total7)  

                gym_use_7 = gym_use.loc[ gym_use['시도명'].str.contains('울산광역시'), ]
                gym_use_7.groupby('군구명')['회원수'].sum()

                fig7 =  px.pie(gym_use_7, names='군구명', values='회원수')
                st.plotly_chart(fig7)

            with con9 :
                # 세종특별자치제
                gym_use_total8 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['세종특별자치시']
                st.subheader('세종특별자치시')
                st.table(gym_use_total8) 

                gym_use_8 = gym_use.loc[ gym_use['시도명'].str.contains('세종특별자치시'), ]
                gym_use_8.groupby('군구명')['회원수'].sum()

                fig8 =  px.pie(gym_use_8, names='군구명', values='회원수')
                st.plotly_chart(fig8)

            with con10 :
                # 제주특별자치도
                gym_use_total9 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['제주특별자치도']
                st.subheader('제주특별자치도')
                st.table(gym_use_total9)  

                gym_use_9 = gym_use.loc[ gym_use['시도명'].str.contains('제주특별자치도'), ]
                gym_use_9.groupby('군구명')['회원수'].sum()

                fig9 =  px.pie(gym_use_9, names='군구명', values='회원수')
                st.plotly_chart(fig9)

            with con11 :
                # 강원도
                gym_use_total10 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['강원도']
                st.subheader('강원도')
                st.table(gym_use_total10) 

                gym_use_10 = gym_use.loc[ gym_use['시도명'].str.contains('강원도'), ]
                gym_use_10.groupby('군구명')['회원수'].sum()

                fig10 =  px.pie(gym_use_10, names='군구명', values='회원수')
                st.plotly_chart(fig10)

            with con12 :
                # 경기도
                gym_use_total11 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['경기도']
                st.subheader('경기도')
                st.table(gym_use_total11) 

                gym_use_11 = gym_use.loc[ gym_use['시도명'].str.contains('경기도'), ]
                gym_use_11.groupby('군구명')['회원수'].sum()

                fig11 =  px.pie(gym_use_11, names='군구명', values='회원수')
                st.plotly_chart(fig11)

            with con13 :
                # 경상남도
                gym_use_total12 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['경상남도']
                st.subheader('경상남도')
                st.table(gym_use_total12)

                gym_use_12 = gym_use.loc[ gym_use['시도명'].str.contains('경상남도'), ]
                gym_use_12.groupby('군구명')['회원수'].sum()

                fig12 =  px.pie(gym_use_12, names='군구명', values='회원수')
                st.plotly_chart(fig12)

            with con14 :
                # 경상북도
                gym_use_total13 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['경상북도']
                st.subheader('경상북도')
                st.table(gym_use_total13)

                gym_use_13 = gym_use.loc[ gym_use['시도명'].str.contains('경상북도'), ]
                gym_use_13.groupby('군구명')['회원수'].sum()

                fig13 =  px.pie(gym_use_13, names='군구명', values='회원수')
                st.plotly_chart(fig13) 

            with con15 :
                #전라북도
                gym_use_total13 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['전라북도']
                st.subheader('전라북도')
                st.table(gym_use_total13)

                gym_use_14 = gym_use.loc[ gym_use['시도명'].str.contains('전라북도'), ]
                gym_use_14.groupby('군구명')['회원수'].sum()

                fig14 =  px.pie(gym_use_14, names='군구명', values='회원수')
                st.plotly_chart(fig14) 

            with con16 :
                # 충청남도
                gym_use_total14 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['충청남도']
                st.subheader('충청남도')
                st.table(gym_use_total14)

                gym_use_15 = gym_use.loc[ gym_use['시도명'].str.contains('충청남도'), ]
                gym_use_15.groupby('군구명')['회원수'].sum()

                fig15 =  px.pie(gym_use_15, names='군구명', values='회원수')
                st.plotly_chart(fig15) 


            with con17 :
                # 충청북도
                gym_use_total15 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['충청북도']
                st.subheader('충청북도')
                st.table(gym_use_total15)

                gym_use_16 = gym_use.loc[ gym_use['시도명'].str.contains('충청북도'), ]
                gym_use_16.groupby('군구명')['회원수'].sum()

                fig16 =  px.pie(gym_use_16, names='군구명', values='회원수')
                st.plotly_chart(fig16) 

        elif choice == menu[4] :
            run_exercise_recommendationt()
    with sp2:
        st.empty()

if __name__ == '__main__' :
    main()