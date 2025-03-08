import streamlit as st


if 'page' not in st.session_state:
    st.session_state.page = "login"   
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'notebooks' not in st.session_state:
    st.session_state.notebooks = {}
if 'current_notebook' not in st.session_state:
    st.session_state.current_notebook = None


import auth
import notebook
import main_page


if st.session_state.page == "login":
    auth.login_page()
elif st.session_state.page == "notebook":
    notebook.notebook_management()
elif st.session_state.page == "main":
    main_page.main_notebook_page()


