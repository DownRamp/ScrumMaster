import streamlit as st
from actions import create_docs


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
        submitted = st.form_submit_button("Submit")

        if submitted:
            # add_data(task, task_status, task_due_date)
            # st.success("Added ::{} ::To Task".format(task))
            create_docs.create(title, description, why, repo_conn, tests, devs, types)
            st.success("Added To Documents")
