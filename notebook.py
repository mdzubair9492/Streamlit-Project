import streamlit as st

def notebook_management():
    st.title("PaperSage: Notebook Management")
    
    
    st.subheader("Create a New Notebook")
    new_notebook = st.text_input("Enter Notebook Name", key="new_nb")
    if st.button("Create Notebook"):
        if new_notebook and new_notebook not in st.session_state.notebooks:
            st.session_state.notebooks[new_notebook] = {"pdfs": [], "notes": []}
            st.success(f"Notebook '{new_notebook}' created!")
            st.session_state.current_notebook = new_notebook
        else:
            st.error("Enter a valid, unique notebook name.")
    
    
    st.subheader("Existing Notebooks")
    if st.session_state.notebooks:
        for nb in list(st.session_state.notebooks.keys()):
            col1, col2 = st.columns([2, 1])
            with col1:
                if st.button(nb, key=f"select_{nb}"):
                    st.session_state.current_notebook = nb
                    st.session_state.page = "main"
            with col2:
                if st.button("Delete", key=f"delete_{nb}"):
                    del st.session_state.notebooks[nb]
                    if st.session_state.current_notebook == nb:
                        st.session_state.current_notebook = None
                    st.success(f"Notebook '{nb}' deleted!")
    else:
        st.info("No notebooks available. Create one above.")
    
   
    if st.button("Logout", key="logout_trigger"):
        st.session_state.page = "login"
        st.session_state.user = None
        for key in ["authentication_status", "name", "username"]:
            if key in st.session_state:
                del st.session_state[key]

