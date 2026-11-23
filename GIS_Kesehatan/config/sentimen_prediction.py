import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "static",
    "model",
    "random_forest_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "static",
    "model",
    "tfidf_vectorizer.pkl"
)

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)


def predict_sentiment(text):
    """
    Mengembalikan:
    positif
    negatif
    """

    vector = tfidf.transform([text])
    hasil = model.predict(vector)[0]

    return hasil.lower()