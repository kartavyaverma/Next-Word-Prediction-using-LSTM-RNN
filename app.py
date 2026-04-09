import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = load_model("models/next_word_model.h5")

# Load tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Set max length (same as training)
max_len = 17   # ⚠️ change this to your actual max_len

# Function to predict next word
def predict_next_word(text):
    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')

    predicted = np.argmax(model.predict(token_list), axis=-1)

    for word, index in tokenizer.word_index.items():
        if index == predicted:
            return word

# UI
st.title("🧠 Next Word Prediction (LSTM)")
st.write("Enter a sentence and predict the next word")

input_text = st.text_input("Enter text:")

if st.button("Predict"):
    if input_text:
        next_word = predict_next_word(input_text)
        st.success(f"Next word: {next_word}")
    else:
        st.warning("Please enter some text")