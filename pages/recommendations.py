import pandas as pd
import numpy as np
import streamlit as st
from utils import capitalize_words

st.set_page_config(page_title="Recommendations")


# Load the data
@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df


df = load_data('./data/spotify_dataset_kaggle.csv')
df = df[["name", "artists", "release_date"]]
df_num = load_data("./data/spotify_numerical_2.csv")
df_num = df_num.set_index("name")

df_num['year'] = df_num['year'] * 10

st.title("Music recommendations")
st.write('Find similar songs based on your preference')

song_search = st.text_input("Search",
                            value="", placeholder='Enter artist or song name...')
song_search = capitalize_words(song_search)


m1 = df["artists"].str.contains(song_search)
m2 = df["name"].str.contains(song_search)
df_search = df[m1 | m2]

if song_search:
    if df_search.empty:
        st.write('No such song or artist')
    else:
        selected_row = st.dataframe(
            df_search, selection_mode="single-row", on_select="rerun", hide_index=True)
        st.write('Please select a box to the left of the title and you will be recommended 5 songs')

        try:
            select_index = selected_row.selection["rows"]

            select_index = select_index[0]
            row = df_search.iloc[select_index]
        except IndexError:
            pass

try:
    song_name = row["name"]
    song = df_num.loc[song_name]
    distances = np.linalg.norm(df_num-song, axis=1)
    recommendations = 5
    indexes = np.argpartition(distances, recommendations)
    st.dataframe(df.iloc[indexes[:recommendations]], hide_index=True)
except IndexError:
    st.write("Select a song by checking the box to the left of the song")
except ValueError:
    st.write("No data")
except NameError:
    pass
