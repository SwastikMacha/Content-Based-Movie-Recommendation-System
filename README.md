🎬 Content-Based Movie Recommendation System

A personalized Movie Recommender System built using Content-Based Filtering and deployed with Streamlit.
The app suggests similar movies based on the metadata (genres, keywords, cast, crew, and overview) of a selected movie and enriches results with posters and details from the TMDB API.

🚀 Features

✅ Content-Based Recommendation using CountVectorizer + Cosine Similarity.<br>
✅ Interactive UI built with Streamlit.<br>
✅ Movie posters, ratings, release date, and overview via TMDB API.<br>
✅ Option to explore Trending Movies (live from TMDB).<br>
✅ Pickle-based persistence for faster app loading (movie_list.pkl & similarity.pkl).

📂 Project Structure

├── content_based_movie_recommendation_system.py   # Preprocessing + model building<br>
├── app.py                                         # Streamlit web application<br>
├── dataset/                                       # Dataset folder<br>
    ├── movies/                                    # Contains tmdb_5000_movies.csv<br>
    └── credits/                                   # Contains tmdb_5000_credits.csv<br>
├── movie_list.pkl                                 # Pickled movie dataset (metadata + tags)<br>
├── similarity.pkl                                 # Pickled cosine similarity matrix<br>
├── requirements.txt                               # Dependencies<br>
└── README.md                                      # Project documentation





