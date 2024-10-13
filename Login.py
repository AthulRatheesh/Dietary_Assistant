import streamlit as st

@st.fragment
def login():
    #st.write("This form is inside a fragment")
    with st.form("Login_Cred"):
        st.write("Sign In:")
        #my_number = st.slider('Pick a number', 1, 10)
        #my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
        username=st.text_input('Username')
        email=st.text_input('Email')
        password=st.text_input('Password', type='password')
        if st.form_submit_button('Submit'):
            if username and email and password:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error('Invalid username and password')
# This is outside the form

if __name__=='__main__':
    #st.set_page_config(page_title="Login", page_icon="���")
    st.title("Sign In:")
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    st.write("You are logged in!")
    st.switch_page("pages/Home.py")