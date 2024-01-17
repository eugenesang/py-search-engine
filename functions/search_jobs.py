import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os


def search_job (input_text):

    file_path = os.path.abspath("./raw-data/cleanJobs.json")
    df_records = pd.read_json(file_path)

    tfidf = TfidfVectorizer(stop_words='english')
    df_records['description'] = df_records['description'].fillna('')
    tfidf_matrix = tfidf.fit_transform(df_records['description'])

    # Transform the input text into a TF-IDF vector
    input_vector = tfidf.transform([input_text])

    # Compute the cosine similarity between the input text and all job descriptions
    cosine_scores = linear_kernel(input_vector, tfidf_matrix).flatten()

    # Get the indices of job descriptions sorted by similarity
    similar_indices = cosine_scores.argsort()[::-1]

    # Return the top 10 most similar job IDs and their descriptions
    top_similar_indices = similar_indices[1:11]
    job_recommendations = [(df_records['_id'].iloc[i], df_records['description'].iloc[i]) for i in top_similar_indices]

    return job_recommendations