# -*- coding: utf-8 -*-
"""
Created on Sat May 17 10:48:21 2025

@author: Sriraman.Rajagopalan
"""

import streamlit as st
from PIL import Image


def main():
    
    bg = "D:/crs/ns/civil/v5_nosave/beta/st/bg/aboutus.jpg"
    
    c1,c2 = st.columns(2)
    
    c1.image(Image.open(bg))

    msg = f''' 
        Most of the standard contracts are too long, which makes people engaging in small projects to work without one in most cases. \n
        This is a condensed standard form of contract with key clauses required for small projects. \n
        We believe this will help in the deterrence towards claims and disputes.
    '''

    c2.write(msg)
    
    st.divider()
    
    msg = f''' 
    Copyright Notice and Proprietary Rights Statement
    © 2026 CoPact. All rights reserved.

    CoPact is a copyrighted product and the exclusive intellectual property of CoPact. All content, designs, source code, documentation, trademarks, service marks, logos, methodologies, workflows, and related materials associated with CoPact are protected under applicable copyright, trademark, and intellectual property laws.

    No part of CoPact may be copied, reproduced, modified, distributed, transmitted, displayed, published, licensed, or used in any form or by any means—electronic, mechanical, photocopying, recording, or otherwise—without the prior written permission of CoPact, except as expressly permitted by applicable law or under a valid licensing agreement.

    Unauthorized use, duplication, or redistribution of CoPact or any of its components may result in civil and/or criminal liability under applicable laws.

    CoPact is provided subject to the terms and conditions outlined in the applicable license agreement. All third-party trademarks, product names, and logos referenced, if any, are the property of their respective owners

    '''
    
    st.caption(msg)
