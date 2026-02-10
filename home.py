# -*- coding: utf-8 -*-
"""
Created on Sat May 17 10:48:21 2025

@author: Sriraman.Rajagopalan
"""

import streamlit as st
from PIL import Image

def main():
    
    st.divider()
    
    bg = "aboutus-1.jpg"
    
    c1,c2 = st.columns(2)
    
    c2.image(Image.open(bg),width=600)

    msg = f''' 
        Many standard contracts are often lengthy and complex, which discourages individuals involved in smaller projects from using formal agreements. \n
        CoPact is a concise, standardized contract format that incorporates the essential clauses required for small-scale projects. It is designed to simplify the contracting process while maintaining legal clarity and professional structure. By providing a practical and accessible framework, CoPact encourages the use of formal agreements even for smaller engagements. \n
        We believe this approach will help minimize misunderstandings, deter potential claims, and reduce the likelihood of disputes, enabling all parties to collaborate with greater confidence and transparency.
    '''

    c1.subheader("What is CoPact?")
    c1.write(msg)
    
    if c1.button("Create my Contract", icon="➕"):
        st.session_state["from_homepage"] = True
        st.rerun()

        
