# 🎬 Content-Based Movie Recommendation System

A personalized **Movie Recommender System** built using **Content-Based Filtering** and deployed with **Streamlit**.  
The app suggests similar movies based on the metadata (genres, keywords, cast, crew, and overview) of a selected movie and enriches results with posters and details from the **TMDB API**.  

---

## 🚀 Features

- ✅ **Content-Based Recommendation** using `CountVectorizer` + `Cosine Similarity`.  
- ✅ **Interactive UI** built with **Streamlit**.  
- ✅ **Movie posters, ratings, release date, and overview** via TMDB API.  
- ✅ Option to explore **Trending Movies** (live from TMDB).  
- ✅ **Pickle-based persistence** for faster app loading (`movie_list.pkl` & `similarity.pkl`).  

---

## 📂 Project Structure
├── content_based_movie_recommendation_system.py &emsp;&emsp; # Preprocessing + model building<br>
├── app.py &emsp;&emsp; # Streamlit web application<br>
├── dataset/ &emsp;&emsp; # Dataset folder<br>
│ ├── movies/ &emsp;&emsp; # Contains tmdb_5000_movies.csv<br>
│ └── credits/ &emsp;&emsp; # Contains tmdb_5000_credits.csv<br>
├── movie_list.pkl &emsp;&emsp; # Pickled movie dataset (metadata + tags)<br>
├── similarity.pkl &emsp;&emsp; # Pickled cosine similarity matrix<br>
├── requirements.txt &emsp;&emsp; # Dependencies<br>
└── README.md &emsp;&emsp; # Project documentation<br>




