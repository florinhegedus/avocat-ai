import streamlit as st
import auth_functions


st.title("Contul meu")

# Show user information
st.header('Informații utilizator:')
st.write(st.session_state.user_info)

# Sign out
st.header('Deconectare:')
st.button(label='Deconectare', on_click=auth_functions.sign_out, type='primary')

# Delete Account
st.header('Șterge cont:')
password = st.text_input(label='Confirmă parola',type='password')
st.button(label='Șterge cont', on_click=auth_functions.delete_account, args=[password], type='primary')