import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rake_nltk import Rake

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')


def read_text(uploaded_file):
    content = uploaded_file.read().decode('utf-8')
    return content


def extract_keywords(text, num_keywords=10):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    r = Rake()
    r.extract_keywords_from_text(" ".join(filtered_words))
    keywords = r.get_ranked_phrases()

    top_keywords = keywords[:num_keywords]
    return top_keywords


def generate_book_summary(book_text, keywords):
    summary = f"The book explores key concepts such as {', '.join(keywords)}. It provides valuable insights into..."
    return summary


# Streamlit app
def main():
    st.title("Book Summary Generator")


