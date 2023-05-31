import streamlit as st
import pickle
import pandas as pd
import requests
movies=pickle.load(open("movies.pkl","rb"))
movies=pd.DataFrame(movies)
angles=pickle.load(open("angles.pkl","rb"))


def fetch_poster(movie_id):
    response= requests.get("") #get the link
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = angles[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    movies_posters=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        movie_id=movies.iloc[i[0]].movie_id
        # movies_posters.append(fetch_poster(movie_id))

    # return recommend_movies,movies_posters
    return recommend_movies
st.title("Movie Recommendation System")

option = st.selectbox(
    'Movie Name?',
    (movies["title"].values))

st.write('You selected:', option)

recom=[]
if st.button("Search"):
    recom=recommend(option)
    for i in recom:
        st.write(i)