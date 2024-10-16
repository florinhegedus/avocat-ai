import streamlit as st
import base64
import fitz
import io

st.set_page_config(
    page_title="Analizator documente",  # Title of the browser tab
    page_icon="📄",  # Icon for the browser tab (document symbol)
    layout="wide",  # Layout of the page ('centered' or 'wide')
    initial_sidebar_state="expanded"  # Sidebar state ('auto', 'expanded', 'collapsed')
)
st.title("Analizator documente")

uploaded_file = st.file_uploader("Alege un fișier PDF", type="pdf")

if uploaded_file is not None:
    # Read the uploaded PDF file
    pdf_data = uploaded_file.read()

    # Open the PDF with PyMuPDF
    doc = fitz.open(stream=pdf_data, filetype='pdf')

    # Get dimensions of the first page to calculate aspect ratio
    first_page = doc.load_page(0)
    rect = first_page.rect
    pdf_width = rect.width
    pdf_height = rect.height
    aspect_ratio = (pdf_height / pdf_width) * 100  # Calculate aspect ratio in percentage

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

    # Display the PDF file using an iframe with dynamic padding based on the aspect ratio
    st.markdown(f'''
        <style>
            .pdf-container {{
                width: 100%;
                height: 0;
                padding-bottom: {aspect_ratio}%; /* Dynamic aspect ratio */
                position: relative;
            }}
            .pdf-container iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border: none;
            }}
        </style>
        <div class="pdf-container">
            <iframe src="{pdf_display}" type="application/pdf"></iframe>
        </div>
        ''', unsafe_allow_html=True)
else:
    st.write("Încarcă un PDF pentru ca aplicația să îl analizeze și să îți ofere un raport.")
