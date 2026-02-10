# -*- coding: utf-8 -*-
"""
Created on Sat May 17 10:48:21 2025

@author: Sriraman.Rajagopalan
"""

import streamlit as st
import datetime,time
from PIL import Image
import contract, aboutus, contactus
import os

# session variables
if "tab" not in st.session_state:
    st.session_state["tab"] = "Home"
    
if "from_homepage" not in st.session_state:
    st.session_state["from_homepage"] = False

st.set_page_config(layout='wide')
st.markdown(""" <style> div.block-container {padding-top: 2rem; padding-bottom: 1rem; } </style> """, unsafe_allow_html=True)

bg = "copact-1.jpg"
now = datetime.datetime.now()

# Display the logo and current date
c1,c2 = st.columns([0.15, 0.85])
c1.image(Image.open(bg))
c1.caption(now.strftime('%A') + ", " + now.strftime("%dth %B, %Y"))

# Page controls
options = ["Home", "Create Contract", "Contact Us", "Quit"]
selection = c2.pills("\t", options, default=st.session_state["tab"])

# Sync selection -> session_state tab
if selection and selection != st.session_state["tab"]:
    st.session_state["tab"] = selection
    st.session_state["from_homepage"] = False
    st.rerun()

if st.session_state["from_homepage"]:
    st.session_state["tab"] = "Create Contract"
    st.session_state["from_homepage"] = False
    st.rerun()

# Render pages
if st.session_state["tab"] == "Home":
    home.main()
elif st.session_state["tab"] == "Create Contract":
    contract.main()
elif st.session_state["tab"] == "Contact Us":
    contactus.main()
elif st.session_state["tab"] == "Quit":
   st.subheader("Are you sure you want to terminate this session ?")
   st.write("\n")
   c1,c2 = st.columns(2)
   btn_close = c1.button("✅",help="Close Application")
    
   if btn_close:    
       with (st.spinner("Closing application ...")):
           time.sleep(2)

            # Clear session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]

       st.success("Session closed. You can safely close the browser tab.")
       st.stop()
else:
    pass
