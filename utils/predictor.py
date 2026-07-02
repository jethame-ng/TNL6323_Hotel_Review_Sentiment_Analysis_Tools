import re
import joblib
import numpy as np
from gensim.models import Word2Vec

# Load models
WORD2VEC_PATH="model/xgboost/word2vec.model"
XGBOOST_PATH="model/xgboost/xgboost_model.pkl"
ENCODER_PATH="model/xgboost/label_encoder.pkl"

word2vec=Word2Vec.load(WORD2VEC_PATH)
xgb=joblib.load(XGBOOST_PATH)
encoder=joblib.load(ENCODER_PATH)

# Text preprocessing
def preprocess(text):
    text=text.lower()
    text=re.sub(r"[^a-zA-Z\s]","",text)
    return re.sub(r"\s+"," ",text).strip()

# Convert review to Word2Vec vector
def review_vector(review):
    vectors=[word2vec.wv[word] for word in review.split() if word in word2vec.wv]

    if vectors:
        return np.mean(vectors,axis=0)

    return np.zeros(word2vec.vector_size)

# Predict sentiment
def predict_sentiment(review):
    review=preprocess(review)
    vector=np.array(review_vector(review)).reshape(1,-1)

    probabilities=xgb.predict_proba(vector)[0]
    prediction=np.argmax(probabilities)
    confidence=probabilities[prediction]
    sentiment=encoder.inverse_transform([prediction])[0]

    return sentiment,confidence

# Split review into sentences
def split_sentences(review):
    return [
        sentence.strip()
        for sentence in re.split(r"[.!?]+",review)
        if sentence.strip()
    ]