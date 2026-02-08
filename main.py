# -*- coding: utf-8 -*-
"""
Created on Sat May 17 10:48:21 2025

@author: Sriraman.Rajagopalan
"""

import streamlit as st
import datetime,time
from PIL import Image
import contract, aboutus
import os

st.set_page_config(layout='wide')

st.markdown(""" <style> div.block-container {padding-top: 3rem; padding-bottom: 1rem; } </style> """, unsafe_allow_html=True)

bg = "copact-1.jpg"
now = datetime.datetime.now()

c1,c2 = st.columns([0.2,0.8])

now = datetime.datetime.now()
# sb1,sb2 = c1.columns(2)
c1.image(Image.open(bg))
c1.caption(now.strftime('%A') + ", " + now.strftime("%dth %B, %Y"))

# c1.caption("📊 Total Downloads today : " + str(contract.st.session_state.totaldownloads))
c1.caption("📊 Total Downloads today : " + str(st.session_state["totaldownloads"]))

t1,t2,t3 = c2.tabs(["Create Contract", "About Us", "Quit"])

with t1:
    contract.main()

with t2:
    aboutus.main()

with t3:
    st.subheader("Are you sure you want to terminate this session ?")
    st.write("\n")
    c1,c2 = st.columns(2)
    btn_close = c1.button("✅",help="Close Application")
    
    if btn_close:    
        with (st.spinner("Closing application ...")):
            time.sleep(2)
                
            import keyboard,psutil
            
            keyboard.press_and_release('ctrl+w')
            pid = os.getpid()
            p = psutil.Process(pid)

            p.terminate()
