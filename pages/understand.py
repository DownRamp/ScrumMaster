import streamlit as st
from fpdf import FPDF

def gen_list(what, how, why, who, when, where, tests, puml_txt):
    results = []
    results.append(f"What ticket?: {what}")
    results.append(f"How will it be done?: {how}")
    results.append(f"Why is it being made?: {why}")
    results.append(f"Who can I ask for help?: {who}")
    results.append(f"Where can I find the repo?: {where}")
    results.append(f"What tests need to be written?: {tests}")
    results.append(f"How long do I have?: {when}")
    results.append(f"Puml text?: {puml_txt}")

def show(arrList):
    for i in arrList:
        st.write(i)

def gen_pdf(arrList):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    for index, i in enumerate(arrList):
        if index%2 == 0:
            pdf.cell(200, 10, txt = i, ln = 1, align = 'L')

        else:
            pdf.cell(200, 10, txt = i,
                     ln = 1, align = 'L')

    # save the pdf with name .pdf
    pdf.output(f"understanding.pdf")
# kinda useless
def app():
    with st.form("my_form"):
        st.title('Create documents')
        what = st.text_input("What Ticket will you be doing?")
        how = st.text_area("What needs to be done?(Seperate with commas)")
        why = st.text_input("Why does it need to be done?")
        who = st.text_area("Who can I ask if I need help?(Separate with commas)")
        when = st.text_area("How much time do I have?")
        where = st.text_input("Which repo?")
        tests = st.text_area("Which tests need to be written(Separate with commas")
        puml_txt = st.text_area("Make puml text (if doesn't already exist)")
        submitted = st.form_submit_button("Submit")

        if submitted:
            arrList = gen_list(what, how, why, who, when, where, tests, puml_txt)
            show(arrList)
            gen_pdf()
            st.success(f"SUCCESS")