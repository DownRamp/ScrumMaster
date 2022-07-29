import streamlit as st
from actions import docs, saver

def show():
    pass

# kinda useless
def app():
    with st.form("my_form"):
        st.title('Create documents')
        what = st.text_input("Ticket")
        how = st.text_area("What needs to be done?(Seperate with commas)")
        why = st.text_input("Why does it need to be done?")
        who = st.text_area("Who can I ask if I need help?(Separate with commas)")
        when = st.text_area("How much time do I have?")
        where = st.text_input("Which repo?")
        tests = st.text_area("Which tests need to be written(Separate with commas")
        puml_txt = st.text_area("Make puml text")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success(f"SUCCESS")