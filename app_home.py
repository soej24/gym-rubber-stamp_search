import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_home() :

    image = Image.open('data/home_img_con.jpg')
    st.image(image, width=None, use_column_width=True)      