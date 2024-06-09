import streamlit as st
import time
import urllib
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

    st.subheader("This app helps to generate blog on favorate topic that you want to write 🖋📃")
    st.divider()

    st.subheader("Blog Topic")

    blog_topic = st.text_input("", placeholder= "Write your Blog topic here")

    if blog_topic:
        st.subheader("Generated Blog")
        # generated_blog = """Data science is the study of data to extract meaningful insights for business. It is a multidisciplinary approach that combines principles and practices from the fields of mathematics, statistics, artificial intelligence, and computer engineering to analyze large amounts of data. This analysis helps data scientists to ask and answer questions like what happened, why it happened, what will happen, and what can be done with the results.
        # Data science is important because it combines tools, methods, and technology to generate meaning from data. Modern organizations are inundated with data; there is a proliferation of devices that can automatically collect and store information. Online systems and payment portals capture more data in the fields of e-commerce, medicine, finance, and every other aspect of human life. We have text, audio, video, and image data available in vast quantities."""
        
        # generated_blog = """Transformer is a neural network architecture used for performing machine learning tasks. In 2017 Vaswani et al. published a paper ” Attention is All You Need” in which the transformers architecture was introduced. Since then, transformers have been widely adopted and extended for various machine learning tasks beyond NLP. The article explores the architecture, working and applications of transformer.
        # Transformer Architecture is a model that uses self-attention that transforms one whole sentence into a single sentence. This is a big shift from how older models work step by step, and it helps overcome the challenges seen in models like RNNs and LSTMs."""
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
            
            time.sleep(2)

        st.write_stream(response_generator(generated_blog))

if __name__ == "__main__":
    main()