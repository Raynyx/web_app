# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:19:06 2023

@author: luigi
"""

import streamlit as st
import base64
import re
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
import buscar as bus
from streamlit_modal import Modal

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Oro</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://images.launchbox-app.com/ec3f1419-609d-482b-b926-37ee146545a2.png",
            width=550)

pokemon = st.text_input("Introduce el pokemon que quieres buscar:")

do = False

if pokemon != '':
    try :
        if bus.maps(pokemon, 'red') == 'not found':
            st.error("Este pokemon no se encuentra en esta generación")
        else:
            bus.maps(pokemon, 'red')
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, 'red')
            st.success("Encontrado")
            file_ = open("pruebaGIF.gif", "rb")
            contents1 = file_.read()
            data_url1 = base64.b64encode(contents1).decode("utf-8")
            file_.close()
            r,l,l2,l3 = st.columns(4)
            with r:
                st.markdown(
                        f'<img src="data:image/gif;base64,{data_url1}"  width="500" height="500" alt="cat gif">',
                        unsafe_allow_html=True)
            with l3:
                st.write("Aquí iria el gif del pokemon")
                st.write("Aquí iria el tipo del  del pokemon")
    except:
        st.error("Este pokemon no existe")
        
if do: 
    with l3:
        select = st.selectbox("Introduce ruta",['Selecciona'] + res_busqueda)
        ok = st.button("BUSCAR")
    if select != 'Selecciona' and ok:
        index =  res_busqueda.index(select)
        modal = Modal(key="Demo Key", title=select)
        with modal.container():
            st.markdown(f"Nivel mínimo de la ruta: {minlevel[index]}")
            st.markdown(f"Nivel máximo de la ruta: {maxlevel[index]}")
            st.markdown(f"Forma de captura: {method[index]}")
            st.markdown(f"Chance: {chance[index]}%")

hide_pages(['Red'])
hide_pages(['Blue'])
hide_pages(['Yellow'])
hide_pages(['Oro'])
hide_pages(['Plata'])
hide_pages(['Cristal'])
hide_pages(['Rubi'])
hide_pages(['Zafiro'])
hide_pages(['Esmera'])
hide_pages(['Diamante'])
hide_pages(['Perla'])
hide_pages(['Platino'])
hide_pages(['Negro'])
hide_pages(['Blanco'])
