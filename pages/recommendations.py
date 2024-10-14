import pandas as pd
import numpy as np
import streamlit as st
from utils import capitalize_words

st.set_page_config(page_title="Recommendations", layout="wide")


# Load the data
@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df

df = load_data('./data/spotify_dataset_kaggle.csv')
st.title("Music recommendations")
st.write('Find similar songs based on your preference')

song_search = st.text_input("Search song by title or speaker", value="", placeholder='Enter artist or song name...')
song_search = capitalize_words(song_search)


m1 = df["artists"].str.contains(song_search)
m2 = df["name"].str.contains(song_search)
df_search = df[m1 | m2]

if song_search:
    st.write(df_search)

