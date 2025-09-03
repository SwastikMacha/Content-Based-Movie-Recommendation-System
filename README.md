🎬 Content-Based Movie Recommendation System

A personalized Movie Recommender System built using Content-Based Filtering and deployed with Streamlit.
The app suggests similar movies based on the metadata (genres, keywords, cast, crew, and overview) of a selected movie and enriches results with posters and details from the TMDB API.

🚀 Features

✅ Content-Based Recommendation using CountVectorizer + Cosine Similarity.
✅ Interactive UI built with Streamlit.
✅ Movie posters, ratings, release date, and overview via TMDB API.
✅ Option to explore Trending Movies (live from TMDB).
✅ Pickle-based persistence for faster app loading (movie_list.pkl & similarity.pkl).

📂 Project Structure

├── content_based_movie_recommendation_system.py   # Preprocessing + model building /n
├── app.py                                         # Streamlit web application
├── dataset/                                       # Dataset folder
    ├── movies/                                    # Contains tmdb_5000_movies.csv
    └── credits/                                   # Contains tmdb_5000_credits.csv
├── movie_list.pkl                                 # Pickled movie dataset (metadata + tags)
├── similarity.pkl                                 # Pickled cosine similarity matrix
├── requirements.txt                               # Dependencies
└── README.md                                      # Project documentation





