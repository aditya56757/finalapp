import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

def generate_article(keyword, writing_style, word_count):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Write an seo optimised article about " + keyword},
            {"role": "user", "content": "The article should be " + writing_style},
            {"role": "user", "content": "The article length should " + str(word_count)},
        ]
    )
    result = ''
    for choice in response['choices']:
        result += choice['message']['content']

    print(result)
    return result

def fun4():
    st.title("Publication Division's  generator")

    keyword = st.text_input("Enter the book keywords.")
    writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
    word_count = st.slider("Select word count:", min_value=40, max_value=1000, step=100, value=300)
    submit_button = st.button("Generate Tweet")

    if submit_button:
        message = st.empty()
        message.text("Busy generating...")
        article = generate_article(keyword, writing_style, word_count)
        message.text("")
        st.write(article)
        st.download_button(
            label="Download article",
            data=article,
            file_name='Article.txt',
            mime='text/txt',
        )
