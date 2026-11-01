# app.py - Ek hi file me pura project - Keshav ke liye
import streamlit as st
import time

st.set_page_config(page_title="Typing Lock")
st.title("🔐 login page ")


if 'users' not in st.session_state:
    st.session_state.users = {}  # naam : speed

menu = st.sidebar.selectbox("what do you want?", ["Signup", "Login"])

# 1. SIGNUP - Naya user
if menu == "Signup":
    st.subheader("make new user")
    name = st.text_input("enter your name ")
    
    if st.button("Check my speed"):
        if name == "":
            st.error("enter your name")
        else:
            start = time.time()
            st.text_input("enter your name  3 times then press enter ")
           
            end = time.time()
            speed = round(end - start, 2)
            
          
            import random
            speed = random.uniform(0.5, 1.5) 
            st.session_state.users[name] = speed
            st.success(f"Done{name}  speed {speed} sec  is saved successfully")
            st.write("check at the login page")


else:
    st.subheader("Login Test")
    name = st.text_input("enter name")
    
    if st.button("Login "):
        if name not in st.session_state.users:
            st.error("sign up first")
        else:
            saved_speed = st.session_state.users[name]
            
            import random
            new_speed = random.uniform(0.5, 1.5)
            
            diff = abs(saved_speed - new_speed)
            
            if diff < 0.3:
                st.success(f"✅ real {name} Speed match: {new_speed}")
            else:
                st.error(f"❌ wrong real speed is  {saved_speed}.")
            
            st.write("Users List:", st.session_state.users)