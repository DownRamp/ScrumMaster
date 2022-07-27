import streamlit as st
from actions import docs, puml

def app():
    st.title('Full view')
    values = docs.fetch_conn()
    full = puml.create_full_puml("fullview",values)
    image = Image.open(full)

    st.image(image, caption='PUML image')
