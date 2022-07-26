import streamlit as st
from actions import tickets

def formation(value):
    st.write(f"Ticket id: {value[0]}")
    st.write(f"Title: {value[1]}")
    st.write(f"Label: {value[2]}")
    st.write(f"Description: {value[3]}")
    st.write(f"Document id: {value[4]}")
    st.write(f"Status: {value[5]}")
    st.write(f"Priority: {value[6]}")
    st.code(f"PUML Text: {value[7]}")
    st.markdown("""---""")

def app():
    st.title('Backlog')
    st.header("Current sprint: ")
    st.markdown("""---""")
    sprint, next, back = tickets.backlog()
    #title, label_val, description, docs, status, prty, puml_txt
    for tic in sprint:
        formation(tic)
    st.header("Next sprint: ")
    st.markdown("""---""")

    for tic in next:
        formation(tic)
    st.header("Current backlog: ")
    st.markdown("""---""")
    for tic in back:
        formation(tic)