import streamlit as st
import time

st.set_page_config(layout="wide")


# Streamed response emulator
def response_generator(response):
    for letter in response:
        yield letter
        time.sleep(0.04)


def main():
    st.title("Blog Generation")

    st.subheader("Blog Title")

    blog_topic = st.text_input("", placeholder= "Write your Blog topic here")

    if blog_topic:
        st.subheader("Generated Blog")
        generated_blog = "Language is the basis for human interaction and communication. Speaking and listening are the direct by-products of human reliance on language. While humans can use language to understand each other, in today’s digital world, they must also interact with machines."

        st.write_stream(response_generator(generated_blog))


if __name__ == "__main__":
    main()