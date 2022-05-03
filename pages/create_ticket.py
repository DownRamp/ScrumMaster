import streamlit as st
from ScrumMaster.actions import create_tickets


def app():
    with st.form("my_form"):
        st.title('Create ticket')
        title = st.text_input("Title")
        label_val = st.text_input("Labels")
        description = st.text_area("Description")
        docs = st.text_input("Docs number")
        priority = st.text_area("Priority (High/Med/Low)")

        submitted = st.form_submit_button("Submit")

        if submitted:
            create_tickets.create(title, label_val, description, docs, priority)
            st.success("Added To Documents")
