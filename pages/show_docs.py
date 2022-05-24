import streamlit as st
from ScrumMaster.actions import tickets

# show small details in list form
def app():
    st.title('Backlog')
    st.write("Current sprint: ")
    docs list = tickets.backlog()
    st.write(sprint)
    st.write("Next sprint: ")
    st.write(next)
    st.write("Current backlog: ")
    st.write(back)