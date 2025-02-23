import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

# App UI
st.set_page_config(page_title="🚢 Titanic Chatbot", layout="centered")
st.title("🚢 Titanic Data Chatbot")

st.markdown(
    """
    **Ask me anything about the Titanic dataset!**  
    Example questions:
    - *What percentage of passengers were male?*
    - *Show me a histogram of passenger ages.*
    - *What was the average ticket fare?*
    - *How many passengers embarked from each port?*
    """
)

st.markdown("---")

# Input field for user queries
question = st.text_input("Type your question:", placeholder="Ask about the Titanic dataset...")

if st.button("Ask"):
    if question:
        response = requests.get("http://127.0.0.1:8000/query/", params={"question": question})
        data = response.json()

        if "answer" in data:
            st.success(data["answer"])

        if "image" in data:
            image_data = base64.b64decode(data["image"])
            image = Image.open(BytesIO(image_data))
            st.image(image, caption="Generated Visualization", use_column_width=True)
    else:
        st.warning("Please enter a question!")

# Sidebar for styling
st.sidebar.title("ℹ️ About")
st.sidebar.info("This chatbot analyzes the Titanic dataset using FastAPI, LangChain, and Streamlit.")
st.sidebar.text("💻👨‍💻 Developer ❤️ Guddu Kumar")
