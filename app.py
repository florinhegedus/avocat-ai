import streamlit as st
import base64

st.title("PDF Viewer App")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
    pdf_display = f'data:application/pdf;base64,{base64_pdf}'
    st.markdown(f'''
        <iframe src="{pdf_display}" width="700" height="1000" type="application/pdf"></iframe>
        ''', unsafe_allow_html=True)
else:
    st.write("Please upload a PDF file to view it here.")
