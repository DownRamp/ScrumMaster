import streamlit as st
from ScrumMaster.actions import docs, puml

def app():
    st.title('Full view')
    values = docs.fetch_conn()
    full = puml.create_puml(values)
    image = Image.open(full)

    st.image(image, caption='PUML image')
