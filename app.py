import streamlit as st


# SESSION STATE 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


login_page = st.Page("pagini_aplicatie/1_Logare.py")
account_page = st.Page("pagini_aplicatie/2_Contul_meu.py")
about_page = st.Page("pagini_aplicatie/3_Despre_aplicație.py")
pdf_page = st.Page("pagini_aplicatie/0_Analizator_documente.py")

default_pages = [login_page, about_page]
user_pages = [pdf_page, account_page, about_page]

if st.session_state.logged_in is False:
    pages = default_pages
else:
    pages = user_pages

pg = st.navigation(pages)
pg.run()
