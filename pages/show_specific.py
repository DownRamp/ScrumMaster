import streamlit as st
from ScrumMaster.actions import docs, puml

# show specific one with call to puml
def app():
    st.title('Show Doc')
    doc = saver.docs()
    puml.create_puml(doc["puml_txt"])
    st.write(doc)
