import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Spotify music recommendations", page_icon=":pie_chart", layout="wide"
)


# Load the data
@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df


st.title("Music recommender")
