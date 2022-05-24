import streamlit as st
from actions import docs

# show small details in list form
def app():
    st.title('Documents')
    docs = docs.fetch()
    st.write(docs)