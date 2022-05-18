import streamlit as st
from ScrumMaster.actions import rolodex

def app():
    st.title('Rolodex')
    rolo = backlog.backlog_fetch()
    st.write(sprint)