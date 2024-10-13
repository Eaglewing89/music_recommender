import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Recommendations", layout="wide")


# Load the data
@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df


st.title("Music recommendations")
