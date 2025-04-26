import streamlit as st
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

st.title("Chatbot Language Testing App")
st.write("Upload your modified JSON file to test the responses.")

uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    records = json.load(uploaded_file)

    for idx, record in enumerate(records):
        st.subheader(f"Conversation {idx+1}")

        base_prompt = record["base_prompt"]
        content = record["content"]
        conversation = record["conversation"]
        completion_prompt = record["completion_prompt"]

        # API call
        completion = client.chat.completions.create(
            model="gpt-4o",
            temperature=0.0,
            messages=[
                {"role": "system", "content": base_prompt + content},
                {"role": "user", "content": conversation},
                {"role": "system", "content": completion_prompt}
            ]
        )

        response_message = completion.choices[0].message

        st.write("**User Question:**")
        st.info(conversation)

        st.write("**Bot Response:**")
        st.success(response_message.content)

        st.markdown("---")