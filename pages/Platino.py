# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:36:55 2023

@author: luigi
"""

import streamlit as st
import base64
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Platino</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://2.bp.blogspot.com/_AOu2rTRHwaI/S5xwpEKLkzI/AAAAAAAAAh0/qVvmt5ob0JU/w1200-h630-p-k-no-nu/POKEMON+PLATINO.png",
            width=550)

pokemon = st.text_input("Introduce el pokemon que quieres buscar:")

if pokemon == 'Y':
    st.success("Hola")
else:
    st.error("Adios")

hide_pages(['RyB'])
hide_pages(['Yellow'])
hide_pages(['OyP'])
hide_pages(['Cristal'])
hide_pages(['RyZ'])
hide_pages(['Esmera'])
hide_pages(['DyP'])
hide_pages(['Platino'])
hide_pages(['NyB'])
hide_pages(['NyB2'])