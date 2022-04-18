import streamlit as st
from actions import backlog


def app():
    st.title('Backlog')

    st.write("Current sprint: ")
    sprint = backlog.sprint_fetch()
    st.write(sprint)
    st.write("Current backlog: ")
    back = backlog.backlog_fetch()
    st.write(back)