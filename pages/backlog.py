import streamlit as st
from ScrumMaster.actions import tickets


def app():
    st.title('Backlog')
    st.write("Current sprint: ")
    sprint, next, back = tickets.backlog()
    st.write(sprint)
    st.write("Next sprint: ")
    st.write(next)
    st.write("Current backlog: ")
    st.write(back)
