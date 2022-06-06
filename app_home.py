import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_home() :

    st.title('Find a Gym to Practice Self-defense')
    st.subheader('자기방어 수련을 위한 체육관 데이터를 분석한 앱')
    st.text('- 가까운 체육관 찾기\n- 연령대별 추천 운동\n- 지역별 스포츠 동호회 참여도')
    st.markdown("***")
    image = Image.open('data/main_img.jpg')
    st.image(image, width=None, use_column_width=True)      