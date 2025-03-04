import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

import streamlit as st
from PIL import Image
from src.image_utils import load_image_from_url
from src.inference import VQAInference

@st.cache_data()
def load_vqa_inference(model_path=None):
    return VQAInference(model_path=model_path)

def footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: black;
            font-size: 14px;
            color: white;
        }
        </style>
        <div class="footer">
            Made with ❤️ by <a href="https://tedoa.vercel.app/" target="_blank">Tadesse Abateneh</a>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    st.title("Visual Question Answering (VQA)")
    st.write("This application uses a pre-trained VQA model to answer questions about images.")

    st.sidebar.title("Model Selection")
    model_path = st.sidebar.text_input("Local Model Path (leave blank for default Hugging Face model)", "")

    vqa_inference = load_vqa_inference(model_path if model_path else None)

    st.sidebar.title("Image Upload")
    image_source = st.sidebar.radio("Select Image Source", ("Upload", "URL"))

    if image_source == "Upload":
        uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
    else:
        image_url = st.sidebar.text_input("Enter Image URL")
        if image_url:
            image = load_image_from_url(image_url)

    if 'image' in locals():
        st.image(image, caption="Uploaded Image", use_container_width=True)
        question = st.text_input("Enter your question about the image:")
        if question:
            answer = vqa_inference.predict(image, question)
            st.write("**Question:**", question)
            st.write("**Answer:**", answer)

    with st.sidebar:
        st.markdown("© 2025 Tadesse Abateneh | [GitHub](https://github.com/tedoaba) | [LinkedIn](https://linkedin.com/in/tadesse-abateneh)")

    footer()

if __name__ == "__main__":
    main()
