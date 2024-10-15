import streamlit as st
import base64
import fitz  # PyMuPDF
import io

st.title("PDF Viewer with Highlighted Words Starting with 'm'")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the uploaded PDF file
    pdf_data = uploaded_file.read()

    # Open the PDF with PyMuPDF
    doc = fitz.open(stream=pdf_data, filetype='pdf')

    # Iterate over each page in the PDF
    for page_num, page in enumerate(doc):
        # Get the words on the page
        word_list = page.get_text("words")  # list of words on page
        for w in word_list:
            word_text = w[4]
            if word_text.lower().startswith('m'):
                # Create a rectangle from the word's bounding box
                rect = fitz.Rect(w[:4])
                # Add a highlight annotation to the page
                highlight = page.add_highlight_annot(rect)
                # Optionally, set color (e.g., yellow)
                highlight.set_colors(stroke=(1, 1, 0))  # RGB colors between 0 and 1
                highlight.update()

    # Save the modified PDF to a BytesIO object
    pdf_bytes = io.BytesIO()
    doc.save(pdf_bytes)
    doc.close()
    pdf_bytes.seek(0)

    # Encode the modified PDF to base64
    base64_pdf = base64.b64encode(pdf_bytes.read()).decode('utf-8')

    # Create a data URI for the PDF file
    pdf_display = f'data:application/pdf;base64,{base64_pdf}'

    # Display the PDF file using an iframe
    st.markdown(f'''
        <iframe src="{pdf_display}" width="700" height="1000" type="application/pdf"></iframe>
        ''', unsafe_allow_html=True)

else:
    st.write("Please upload a PDF file to view it here.")
