import pickle
import streamlit as st
import pandas as pd
import requests
import os
import gdown

# ========================
# TMDB API Config
# ========================
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
BASE_URL = "https://api.themoviedb.org/3"
IMG_BASE_URL = "https://image.tmdb.org/t/p/w500/"

# ========================
# Utility Functions
# ========================

@st.cache_data
def fetch_movie_details(movie_id):
    """Fetch movie details including poster, overview, and rating."""
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url).json()
    poster_path = response.get('poster_path')
    full_poster = IMG_BASE_URL + poster_path if poster_path else "https://via.placeholder.com/500x750?text=No+Image"
    overview = response.get('overview', 'No description available.')
    rating = response.get('vote_average', 'N/A')
    release_date = response.get('release_date', 'Unknown')
    return full_poster, overview, rating, release_date

def recommend(movie, movies, similarity):
    """Recommend top 5 similar movies based on similarity matrix."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        poster, overview, rating, release_date = fetch_movie_details(movie_id)
        recommended_movies.append({
            "title": movies.iloc[i[0]].title,
            "poster": poster,
            "overview": overview,
            "rating": rating,
            "release_date": release_date
        })
    return recommended_movies

@st.cache_data
def fetch_trending_movies():
    """Fetch trending movies from TMDB."""
    url = f"{BASE_URL}/trending/movie/week?api_key={API_KEY}"
    response = requests.get(url).json()
    results = response.get("results", [])
    trending = []
    for movie in results[:10]:
        poster = IMG_BASE_URL + movie['poster_path'] if movie.get('poster_path') else "https://via.placeholder.com/500x750?text=No+Image"
        trending.append({
            "title": movie['title'],
            "poster": poster,
            "overview": movie.get('overview', 'No description available.'),
            "rating": movie.get('vote_average', 'N/A'),
            "release_date": movie.get('release_date', 'Unknown')
        })
    return trending

@st.cache_data
def load_data():
    """Load movies and similarity matrix."""
    # Load movie list
    movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    # Download similarity.pkl if not present
    if not os.path.exists("similarity.pkl"):
        gdown.download("YOUR_GOOGLE_DRIVE_SHARED_LINK", "similarity.pkl", quiet=False)

    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

# ========================
# Load Data
# ========================
movies, similarity = load_data()

# ========================
# Streamlit UI
# ========================
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎥 Movie Recommender System")
st.markdown("Get personalized recommendations, trending movies, and more!")

# Sidebar for navigation
option = st.sidebar.radio("Choose an option:", ["Recommend Similar Movies", "Trending Movies"])

if option == "Recommend Similar Movies":
    selected_movie_name = st.selectbox("Choose a movie:", movies['title'].values)

    if st.button("Show Recommendations"):
        recommendations = recommend(selected_movie_name, movies, similarity)
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(recommendations[idx]["poster"])
                st.markdown(f"**{recommendations[idx]['title']}**")
                st.caption(f"⭐ {recommendations[idx]['rating']} | 📅 {recommendations[idx]['release_date']}")
                with st.expander("About"):
                    st.write(recommendations[idx]['overview'])

elif option == "Trending Movies":
    trending = fetch_trending_movies()
    st.subheader("🔥 Trending This Week")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(trending[idx]["poster"])
            st.markdown(f"**{trending[idx]['title']}**")
            st.caption(f"⭐ {trending[idx]['rating']} | 📅 {trending[idx]['release_date']}")
            with st.expander("About"):
                st.write(trending[idx]['overview'])
