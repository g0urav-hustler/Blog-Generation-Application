import streamlit as st
import time
import urllib.request
import json

st.set_page_config(page_title="Blog Generation App",layout="wide")

url = "https://3obv4jibod.execute-api.us-east-1.amazonaws.com/first_stage/generate-blog"

# Streamed response emulator
def response_generator(response):
    for letter in response:
        yield letter
        time.sleep(0.02)


def main():
    st.title("Blog Generation App")

    st.subheader("This app helps to generate blog on desired topic that you want to write 🖋📃")
    st.divider()

    st.subheader("Blog Topic")

    blog_topic = st.text_input("", placeholder= "Write your Blog topic here")

    if blog_topic:
        
            try:   
                st.subheader("Generated Blog")
                with st.spinner("Generating the blog 🪄"):
                    data = {
                        "blog_topic": str(blog_topic)
                    }

                    data = json.dumps(data)
                    data = str(data)
                    data = data.encode("utf-8")
                    
                    response = urllib.request.urlopen(url = url, data = data)

                    model_response = response.read()

                    model_response = json.loads(model_response)

                    generated_blog = model_response['body']

                st.write_stream(response_generator(generated_blog))
            
            except Exception as e:

                st.warning("App is under maintenance due to service charges.")


if __name__ == "__main__":
    main()