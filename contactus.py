# -*- coding: utf-8 -*-
"""
Created on Sat May 17 10:48:21 2025

@author: Sriraman.Rajagopalan
"""

import streamlit as st


def main():
    
    msg = f''' 
        We would love to hear from you. We welcome you to provide your feedback on Copact and help us with further developments. \n

        📝         https://docs.google.com/forms/d/e/1FAIpQLSdVrVJVpf9c1bddvXqfJ9yWPPg5CejR39GxIM0XKni4qy2GMQ/viewform?usp=publish-editor
        
        📩         drsunder2025@outlook.com
    '''

    st.subheader("Your Voice Matters")
    st.write(msg)
    
    st.divider()
    
    msg = f''' 
    Copyright Notice and Proprietary Rights Statement
    © 2026 CoPact. All rights reserved.

    CoPact is a copyrighted product and the exclusive intellectual property of CoPact. \n
    All content, designs, source code, documentation, trademarks, service marks, logos, methodologies, workflows, and related materials associated with CoPact are protected under applicable copyright, trademark, and intellectual property laws.

    No part of CoPact may be copied, reproduced, modified, distributed, transmitted, displayed, published, licensed, or used in any form or by any means—electronic, mechanical, photocopying, recording, or otherwise—without the prior written permission of CoPact, except as expressly permitted by applicable law or under a valid licensing agreement.

    Unauthorized use, duplication, or redistribution of CoPact or any of its components may result in civil and/or criminal liability under applicable laws.

    CoPact is provided subject to the terms and conditions outlined in the applicable license agreement. All third-party trademarks, product names, and logos referenced, if any, are the property of their respective owners

    '''
    
    st.subheader("Copyright Notice")
    st.caption(msg)

    
    