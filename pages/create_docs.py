import streamlit as st
import re

from actions import docs

ptext="""(*) --> 'User' as user
user --> 'Website' as web
user --> 'Sprint update (POST)' as upsprint
web --> 'Create doc (POST)' as doc
    --> 'API' as api
web --> 'Create ticket (POST)' as ticket
    --> api
web --> 'Update doc (POST)' as updoc
    --> api
web --> 'Update ticket (POST)' as upticket
    --> api
web --> 'Hiring (POST)' as ticket
    --> api
web --> 'Fetch sprint updates (GET)' as sprint
    --> api
web --> 'Backlog (GET)' as ticket
    --> api
web --> 'Fetch full view (GET)' as full
    --> 'Create puml' as puml
    --> api
web --> 'Rolodex (GET)' as rolo
    --> api
web --> 'Show docs (GET)' as show
    --> puml
    --> api
api --> (*)"""

# escape special characters
def clean_up(value):
    return re.escape(value)

def app():
    with st.form("my_form"):
        st.title('Create documents')
        title = st.text_input("Title")
        description = st.text_area("Description")
        why = st.text_input("Background and why")
        #1,2,3
        repo_conn = st.text_area("Input all program connections by doc id(Separate with commas)")
        tests = st.text_area("Tests to be created")
        devs = st.text_area("Developers with knowledge on this (Separate with commas)")
        types = st.text_input("Type(Function, repo, tool)")

        puml_txt = st.text_area("Put in your puml text here")
        st.markdown("Example")
        st.code(ptext)

        submitted = st.form_submit_button("Submit")

        if submitted:
            id = docs.create(title, description, why, repo_conn, tests, devs, types, clean_up(puml_txt).split("\n"))
            st.success(f"Added To Documents with id: {id}")
