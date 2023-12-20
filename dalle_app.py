import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )
    image_url = response["data"][0]["url"]
    return image_url

def fun3():
    st.title("DPD Publication Image Generator")

    # Get user input
    prompt = st.text_input("Enter a prompt for image generation:")

    # Generate and display the image
    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            image_url = generate_image(prompt)
            st.image(image_url, caption="Generated Image", use_column_width=True)

