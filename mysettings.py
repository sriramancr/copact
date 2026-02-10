# -*- coding: utf-8 -*-
"""
@author: Sriraman.Rajagopalan
"""

import streamlit as st

date_formats = ["DD-MM-YYYY", "DD/MM/YYYY", "YYYY-MM-DD", "YYYY/MM/DD", "DD.MM.YYYY", "MM-DD-YYYY", 
                "MM/DD/YYYY", "YYYY-MM-DD", "Mon DD, YYYY", "DD Mon YYYY"]

def main():
    st.divider()
    
    c1,c2,c3 = st.columns([0.1,0.2,0.7])
    
    dt_format = c2.selectbox("Date Format", date_formats)
    
    # st.write("before change: session state date format = ", st.session_state["dateformat"])
    
    if dt_format !=  st.session_state["dateformat"]:
        st.session_state["dateformat"] = dt_format

    # st.write("after change: session state date format = ", st.session_state["dateformat"])