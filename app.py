import streamlit as st

st.set_page_config(page_title="GenAI Phishing URL Detector", page_icon="🛡️")
st.title("🛡️ GenAI + VirusTotal Phishing URL Detector")

url = st.text_input("Enter a URL to check")

if st.button("Analyze"):
    if not url:
        st.warning("Please paste a URL first.")
    else:
        st.info("Demo only: logic to be added.")
        st.write(f"URL received: {url}")
