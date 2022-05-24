import streamlit as st
from actions import tickets


def app():
    with st.form("my_form"):
        st.title('Create ticket')
        title = st.text_input("Title")
        label_val = st.text_input("Labels")
        description = st.text_area("Description")
        docs = st.text_input("Docs number")
        status = st.text_input("Status (1 - current, 2 - Next sprint, 3 - backlog,  0 - Finished)")
        priority = st.text_area("Priority (High/Med/Low)")
        puml_text = st.text_area("PUML text")

        submitted = st.form_submit_button("Submit")

        if submitted:
            response = tickets.update(title, label_val, description, docs, status, prty, puml_txt.split("\n"), id)
            st.success(f"Updated Ticket: {response}")