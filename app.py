import streamlit as st
import pickle
import requests

movies = pickle.load(open("app/movies_list.pkl", "rb"))
similarity = pickle.load(open("app/similarity.pkl","rb"))

st.title("Movie Recommendation System")
st.write("Get Movie recommendations")


movies_list=movies['title'].values

API_KEY = "7374f3da35a66d8ce0eb0adf51693984"

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

        return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"

select_value=st.selectbox("Select any Movie", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommend_movies=[]
    recommend_posters=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]]['id']
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movies_id))
    return recommend_movies, recommend_posters


if st.button("show recommendations"):
    movie_name, movie_poster=recommend(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        if movie_poster[0]:
            st.image(movie_poster[0])

    with col2:
        st.text(movie_name[1])
        if movie_poster[1]:
            st.image(movie_poster[1])

    with col3:
        st.text(movie_name[2])
        if movie_poster[2]:
            st.image(movie_poster[2])

    with col4:
        st.text(movie_name[3])
        if movie_poster[3]:
            st.image(movie_poster[3])

    with col5:
        st.text(movie_name[4])
        if movie_poster[4]:
            st.image(movie_poster[4])


