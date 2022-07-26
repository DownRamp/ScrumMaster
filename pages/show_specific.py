import streamlit as st
from actions import docs, puml

# show specific one with call to puml
def app():
    st.title('Show Doc')
    doc = saver.docs()
    st.image(puml.create_puml(doc[8]))
    st.write(doc)
