# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:16:56 2023

@author: luigi
"""

import streamlit as st
import base64
import re
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
import buscar as bus
from streamlit_modal import Modal

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Platino</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://2.bp.blogspot.com/_AOu2rTRHwaI/S5xwpEKLkzI/AAAAAAAAAh0/qVvmt5ob0JU/w1200-h630-p-k-no-nu/POKEMON+PLATINO.png",
            width=550)

pokemon = st.text_input("Introduce el pokemon que quieres buscar:")

do = False

if pokemon != '':
    try :
        if bus.maps(pokemon, 'platinum') == 'not found':
            st.error("Este pokemon no se encuentra en esta generación")
        else:
            bus.maps(pokemon, 'platinum')
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, 'platinum')
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
                bus.get_sprite(pokemon)
                file_ = open("spriteGIF.gif", "rb")
                contents2 = file_.read()
                data_url2 = base64.b64encode(contents2).decode("utf-8")
                file_.close()
                st.markdown(f'<img src="data:image/gif;base64,{data_url2}"  width="100" height="100" alt="cat gif">',
                            unsafe_allow_html=True)

                bus.get_audio(pokemon)
                audio_file = open('crie.mp3', 'rb')
                audio_bytes = audio_file.read()
                
                st.audio(audio_bytes, format='audio/mp3')
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
