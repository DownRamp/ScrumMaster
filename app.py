import streamlit as st
from multiapp import MultiApp
from pages import create_ticket, create_docs, full_view, rolodex, backlog, show_docs, show_specific, update_doc, update_ticket

app = MultiApp()

# Add all your application here
app.add_app("Backlog", backlog.app)
app.add_app("Show Documents", show_docs.app)
app.add_app("Show Specific docs", show_specific.app)
app.add_app("Full View", full_view.app)
app.add_app("Create ticket", create_ticket.app)
app.add_app("Create docs", create_docs.app)
app.add_app("Update ticket", update_ticket.app)
app.add_app("Update docs", update_ticket.app)
app.add_app("Rolodex", rolodex.app)

# The main app
app.run()