import streamlit as st
import auth_functions


st.title("Logare")

col1,col2,col3 = st.columns([1,2,1])

# Authentication form layout
do_you_have_an_account = col2.selectbox(label='Aveți cont?',options=('Da','Nu','Mi-am uitat parola'))
auth_form = col2.form(key='Authentication form',clear_on_submit=False)
email = auth_form.text_input(label='Email')
password = auth_form.text_input(label='Password',type='password') if do_you_have_an_account in {'Da','Nu'} else auth_form.empty()
auth_notification = col2.empty()

# Sign In
if do_you_have_an_account == 'Da' and auth_form.form_submit_button(label='Logare',use_container_width=True,type='primary'):
    with auth_notification, st.spinner('Logare în curs'):
        auth_functions.sign_in(email,password)

# Create Account
elif do_you_have_an_account == 'Nu' and auth_form.form_submit_button(label='Creează cont',use_container_width=True,type='primary'):
    with auth_notification, st.spinner('Creating account'):
        auth_functions.create_account(email,password)

# Password Reset
elif do_you_have_an_account == 'Mi-am uitat parola' and auth_form.form_submit_button(label='Resetează parola',use_container_width=True,type='primary'):
    with auth_notification, st.spinner('Se trimite un link de resetare a parolei...'):
        auth_functions.reset_password(email)

# Authentication success and warning messages
if 'auth_success' in st.session_state:
    auth_notification.success(st.session_state.auth_success)
    del st.session_state.auth_success
elif 'auth_warning' in st.session_state:
    auth_notification.warning(st.session_state.auth_warning)
    del st.session_state.auth_warning