import streamlit as st
import time


st.set_page_config(page_title="PaperSage", layout="wide")

def simulate_llm_response(prompt):
    time.sleep(1)  
    return f"Simulated answer for: '{prompt}'"

def main_notebook_page():
    st.title(f"PaperSage: Notebook - {st.session_state.current_notebook}")

    
    st.write("---")

    
    col1, col2, col3 = st.columns(3, gap="large")

    
    with col1:
        st.header("Upload Research Paper")
        uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])
        if uploaded_file is not None:
            st.session_state.notebooks[st.session_state.current_notebook]["pdfs"].append(uploaded_file.name)
            st.success(f"Uploaded: {uploaded_file.name}")
        
        st.markdown("### Uploaded Papers")
        papers = st.session_state.notebooks[st.session_state.current_notebook]["pdfs"]
        if papers:
            for paper in papers:
                st.write(f"- {paper}")
        else:
            st.write("No papers uploaded yet.")

   
    with col2:
        st.header("Ask a Question")
        user_query = st.text_input("Your question about the paper", key="query")
        if st.button("Submit Query"):
            if user_query:
                st.info("Processing your query...")
                response = simulate_llm_response(user_query)
                st.session_state.chat_history.append(("User", user_query))
                st.session_state.chat_history.append(("PaperSage", response))
        
        st.markdown("### Chat History")
        for role, msg in st.session_state.chat_history:
            if role == "User":
                st.markdown(f"**You:** {msg}")
            else:
                st.markdown(f"**PaperSage:** {msg}")

    
    with col3:
        st.header("Notes")
        note_input = st.text_area("Write your note here", key="note")
        
        if st.button("Save Note"):
            if note_input:
                st.session_state.notebooks[st.session_state.current_notebook]["notes"].append(note_input)
                st.success("Note saved!")
        
        if st.button("Generate Auto-Note"):
            auto_note = simulate_llm_response("Generate note for current paper")
            st.session_state.notebooks[st.session_state.current_notebook]["notes"].append(auto_note)
            st.success("Auto-note generated!")
        
        st.markdown("### Saved Notes")
        notes = st.session_state.notebooks[st.session_state.current_notebook]["notes"]
        if notes:
            for idx, note in enumerate(notes, start=1):
                st.write(f"{idx}. {note}")
        else:
            st.write("No notes available yet.")

   
    if st.button("Back to Notebook Management"):
        st.session_state.page = "notebook"



