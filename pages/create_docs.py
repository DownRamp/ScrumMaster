import streamlit as st
from actions import docs


def app():
    with st.form("my_form"):
        st.title('Create documents')
        title = st.text_input("Title")
        description = st.text_area("Description")
        why = st.text_input("Background and why")
        repo_conn = st.text_area("Input all repos connected to this(Separate with commas)")
        tests = st.text_area("Tests to be created")
        devs = st.text_area("Developers with knowledge on this (Separate with commas")
        types = st.text_input("Type(Function, repo, tool)")
        puml_txt = st.text_area("Put in your puml text here")

        submitted = st.form_submit_button("Submit")

        if submitted:
            id = docs.create(title, description, why, repo_conn, tests, devs, types, puml_txt.split("\n"))
            st.success(f"Added To Documents with id: {id}")
