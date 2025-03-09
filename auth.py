import streamlit as st
import streamlit_authenticator as stauth
import os
import yaml
import time
from yaml.loader import SafeLoader


def load_credentials(file_path="credentials.yaml"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            config = yaml.load(file, Loader=SafeLoader)
    else:
        
        config = {
            'credentials': {
                'usernames': {}
            },
            'cookie': {
                'expiry_days': 30,
                'key': 'some_signature_key',
                'name': 'some_cookie_name'
            }
        }
    return config

def save_credentials(config, file_path="credentials.yaml"):
    with open(file_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)


def login_page():
    st.title("PaperSage: User Registration / Login")
    
    action = st.selectbox("Select Action", ["Login", "Register"])
   
    config = load_credentials()

    if action == "Register":
        st.header("User Registration")
        new_username = st.text_input("Enter new username")
        new_password = st.text_input("Enter new password", type="password")
        
        if st.button("Register"):
            if new_username and new_password:
                if new_username in config['credentials']['usernames']:
                    st.error("Username already exists!")
                else:
                    
                    hashed_passwords = stauth.Hasher.hash_list([new_password])
                    
                    config['credentials']['usernames'][new_username] = {
                        'email': f"{new_username}@example.com",  
                        'name': new_username,
                        'password': hashed_passwords[0]
                    }
                    save_credentials(config)
                    st.success("User registered successfully!")
                    
                    st.session_state.page = "login"
            else:
                st.error("Please fill in both fields.")
    else:  
        st.header("User Login")
        
        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days']
        )
        
        
        authenticator.login(location="main", fields={"Login": "Sign In"})
        
       
        if "authentication_status" in st.session_state:
            if st.session_state["authentication_status"]:
                st.success(f"Welcome *{st.session_state['name']}*")
                st.session_state.user = st.session_state["username"]
                st.session_state.page = "notebook"  
            elif st.session_state["authentication_status"] is False:
                st.error("Username/password is incorrect")
            elif st.session_state["authentication_status"] is None:
                st.warning("Please enter your username and password")
        else:
            st.warning("Awaiting login...")



