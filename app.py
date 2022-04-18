import streamlit as st
from multiapp import MultiApp
from pages import create_ticket, create_docs, full_view, rolodex, backlog, show_docs

app = MultiApp()

# Add all your application here
app.add_app("Create ticket", create_ticket.app)
app.add_app("Create docs", create_docs.app)
app.add_app("Full View", full_view.app)
app.add_app("Rolodex", rolodex.app)
app.add_app("Backlog", backlog.app)
app.add_app("Show Documents", show_docs.app)


# The main app
app.run()