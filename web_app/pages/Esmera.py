# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:29:26 2023

@author: luigi
"""

import streamlit as st
import base64
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Esmeralda</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://images.wikidexcdn.net/mwuploads/wikidex/9/9e/latest/20090224004230/Pok%C3%A9mon_Esmeralda.png",
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