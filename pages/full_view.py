import streamlit as st
from ScrumMaster.actions import docs, puml

def app():
    st.title('Full view')
    full = docs.fetch_conn()
    st.write(full)
