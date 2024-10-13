import streamlit as st

if not st.session_state['logged_in']:
    st.switch_page('')
else:
    st.title("Welcome!")
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.switch_page('Login.py')
