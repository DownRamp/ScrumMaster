import streamlit as st
import re

from actions import tickets

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

def clean_up(value):
    return re.escape(value)

def app():
    with st.form("my_form"):
        st.title('Create ticket')
        title = st.text_input("Title")
        label_val = st.text_input("Labels")
        description = st.text_area("Description")
        docs = st.text_input("Docs number")
        status = st.text_input("Status (1 - current, 2 - Next sprint, 3 - backlog,  0 - Finished)")
        priority = st.text_area("Priority (High/Med/Low)")
        puml_txt = st.text_area("PUML text")
        st.markdown("Example")
        st.code(ptext)
        submitted = st.form_submit_button("Submit")

        if submitted:
            list = clean_up(puml_txt).split("\n")
            print(list)
            id = tickets.create(title, label_val, description, docs, status, priority, list)
            st.success(f"Added To Tickets with id: {id}")