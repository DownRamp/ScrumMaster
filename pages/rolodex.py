import streamlit as st
from actions import rolodex

def app():
    # create page
    st.title('Rolodex')
    st.write("Current employees: ")
    ppl = rolodex.fetch()
    st.write(ppl)

    # show open positions
    with st.form("my_form"):
        st.title('Add an employee')
        full_name = st.text_input("Full Name")
        title = st.text_input("Work Title")
        email = st.text_input("Email")

        submitted = st.form_submit_button("Submit")

        if submitted:
            id = rolodex.create(full_name, title, email)
            st.success(f"Added To Documents with id: {id}")