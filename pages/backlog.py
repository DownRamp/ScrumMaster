import streamlit as st
from actions import tickets, updates
from datetime import date

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
    upds = updates.fetch()
    with st.sidebar:
        st.write(upds)
        with st.form("my_form"):
            st.title('Add an update')
            full_name = st.text_input("Full Name")
            blockers = st.text_input("Blockers")
            today_work = st.text_input("Todays work")
            yesterday = st.text_input("Yesterday work")

            submitted = st.form_submit_button("Submit")
            if submitted:
                today = date.today().strftime("%d/%m/%Y")
                id = updates.create(today, yesterday, today_work, blockers, full_name)
                st.success(f"Added To Updates Successfully")

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