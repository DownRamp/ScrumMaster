import streamlit as st
from actions import docs

# show small details in list form
def app():
    st.title('Documents')
    documents = docs.fetch()
    for doc in documents:
        st.markdown(f"<h3 style='text-align: center; '><u><i><b>Document Id</b></i>: {doc[0]}</u></h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Title</b></i>: {doc[1]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Description</b></i>: {doc[2]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Why</b></i>: {doc[3]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Repo Connections</b></i>: {doc[4]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Tests</b></i>: {doc[5]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Developers with knowledge</b></i>: {doc[6]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; '><i><b>Type</b></i>: {doc[7]}</p>", unsafe_allow_html=True)
        st.code(f"PUML Text: {doc[8]}")
        st.markdown("""---""")

    st.markdown("To see puml displayed go to 'Show Specific Docs'")