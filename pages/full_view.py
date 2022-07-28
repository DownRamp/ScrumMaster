import streamlit as st
from actions import docs, puml

def app():
    st.title('Full view')
    values = docs.fetch_conn()
    st.image(puml.create_full_puml("fullview",values))
