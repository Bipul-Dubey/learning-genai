import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st


## mapping of words index back to words for understanding
word_index = imdb.get_word_index()
# word_index
## reverse word index
reverse_word_index = {value: key for key, value in word_index.items()}


model=load_model("simple_rnn_imdb.h5")

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, "?") for i in encoded_review])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review


### prediction function
def predict_sentiment(review):
    preprocess_input = preprocess_text(review)

    prediction = model.predict(preprocess_input,verbose=0)
    score = prediction[0][0]
    sentiment = "Positive" if score >= 0.5 else "Negative"

    return sentiment, score 


st.set_page_config(
    page_title="Movie Review System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Movie Review System")

st.header("👤 Review")

user_input = st.text_area("Movie Review")

if user_input.strip():
    if st.button("Submit Review"):
        st.success("Review submitted successfully!")
        # Add your review processing logic here
        preprocessed_text = preprocess_text(user_input)
        
        prediction = model.predict(preprocessed_text,verbose=0)
        score = prediction[0][0]
        sentiment = "Positive" if score >= 0.5 else "Negative"

        st.success(f"Sentiment: {sentiment}")
        st.write(f"Confidence Score: {score:.2%}")

else:
    st.info("Please enter a movie review.")

