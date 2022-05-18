import streamlit as st
from ScrumMaster.actions import backlog


def app():
    st.title('Backlog')
    st.write("Current sprint: ")
    sprint, back = backlog.backlog_fetch()
    st.write(sprint)
    st.write("Current backlog: ")
    st.write(back)
