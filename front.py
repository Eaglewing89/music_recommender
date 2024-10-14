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

df = load_data('./data/spotify_dataset_kaggle.csv')

st.title("Music recommender")
st.write("#### Discover your next favorite song with our music recommendation app. Whether you're looking to explore new genres, find tracks that match your current mood, or simply expand your playlist, we've got you covered!Our app is designed to curate personalized music suggestions based on your preferences, listening history, or even specific moods and activities. With just a few clicks, you can:")
st.markdown("- Explore New Genres – Dive into a world of music you haven't yet discovered.")
st.markdown("- Find Mood-based Playlists – Whether you’re feeling upbeat, mellow, or somewhere in between, we'll recommend tracks that resonate.")
st.markdown("- Tailor Recommendations – Refine your choices to match your unique taste or try something entirely new!")
