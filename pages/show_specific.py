import streamlit as st
from actions import puml, saver

# show specific one with call to puml
def app():
    st.title('Show Doc')
    documents = saver.docs()

    with st.form("my_form"):
        id = st.text_input("Enter Document id")
        submitted = st.form_submit_button("Submit")

        if submitted:
            doc = documents.get(int(id))
            st.image(puml.create_puml(doc.title, doc.puml_txt))
            st.write(doc)