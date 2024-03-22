import streamlit as st
import requests

st.title('Review Analysis')
review_text = st.text_area("Enter the review text:")

fastapi_endpoint = 'http://endpoints:8118/analysis-review'

if st.button('Analyze'):
    if not review_text:
        st.error("Please enter some text for analysis.")
    else:
        response = requests.post(fastapi_endpoint, json={"text": review_text})
        if response.status_code == 200:
            result = response.json()
            st.success(f"Analysis Result: {result['data']}")
        else:
            st.error("Error in analysis.")
