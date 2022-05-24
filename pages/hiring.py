import streamlit as st
from actions import hiring

def app():
    # create page
    st.title('Hiring')
    st.write("Current job postings: ")
    hires = hiring.fetch()
    st.write(hires)

    # show open positions
    with st.form("my_form"):
        st.title('Add a job posting')
        title = st.text_input("Title")
        label_val = st.text_input("Team")
        description = st.text_input("Full description of job")

        submitted = st.form_submit_button("Submit")

        if submitted:
            id = hirings.create(title, label_val, description)
            st.success(f"Added To Documents with id: {id}")