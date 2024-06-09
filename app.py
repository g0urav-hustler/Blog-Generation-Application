import streamlit as st
import time

st.set_page_config(page_title="Blog Generation App",layout="wide")


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
        generated_blog = """Data science is the study of data to extract meaningful insights for business. It is a multidisciplinary approach that combines principles and practices from the fields of mathematics, statistics, artificial intelligence, and computer engineering to analyze large amounts of data. This analysis helps data scientists to ask and answer questions like what happened, why it happened, what will happen, and what can be done with the results.
        Data science is important because it combines tools, methods, and technology to generate meaning from data. Modern organizations are inundated with data; there is a proliferation of devices that can automatically collect and store information. Online systems and payment portals capture more data in the fields of e-commerce, medicine, finance, and every other aspect of human life. We have text, audio, video, and image data available in vast quantities."""
        
        with st.spinner("Generating the blog 🪄"):
            time.sleep(2)
            
        st.write_stream(response_generator(generated_blog))

if __name__ == "__main__":
    main()