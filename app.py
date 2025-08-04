import os
import joblib
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer


def load_model(path):
    return joblib.load(path)

# --- Title ---
st.title("📩 Email Spam Classifier")

# --- Input box ---
user_input = st.text_area("Enter the email message here:")

# --- Load model using absolute path ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # root directory
model_path = os.path.join(BASE_DIR, 'outputs', 'spam_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'outputs', 'vectorizer.pkl')

# --- File existence check ---
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    st.error("Model or vectorizer file not found. Make sure both exist in the 'outputs/' folder.")
else:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    # --- Predict ---
    if st.button("Predict"):
        if not user_input.strip():
            st.warning("Please enter a message first.")
        else:
            user_input_vec = vectorizer.transform([user_input])
            prediction = model.predict(user_input_vec)[0]

            if prediction == "spam":
                st.error("🚫 This email is likely SPAM!")
            else:
                st.success("✅ This email looks SAFE (not spam).")
