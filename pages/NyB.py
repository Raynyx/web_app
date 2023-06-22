# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:45:28 2023

@author: luigi
"""

import streamlit as st
import base64
import re
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
import buscar as bus
from streamlit_modal import Modal

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Negro y Blanco</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://pokemonalpha.xyz/wp-content/uploads/Pok%C3%A9mon-Negro-y-Blanco-portadas.png",
            width=550)

pokemon = st.text_input("Introduce el pokemon que quieres buscar:")

do = False

region = st.radio("Selecciona el juego:",["black","white"])

if pokemon != '':
    try :
        if bus.maps(pokemon, region) == 'not found':
            st.error("Este pokemon no se encuentra en esta generación")
        else:
            bus.maps(pokemon, region)
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, region)
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
            with 1:
                bus.get_audio(pokemon)
                audio_file = open('crie.mp3', 'rb')
                audio_bytes = audio_file.read()
                
                st.audio(audio_bytes, format='audio/mp3')
                
                st.write("Aquí iria el tipo del  del pokemon")
    except:
        st.error("Este pokemon no existe")
        
if do: 
    with l3:
        select = st.selectbox("Introduce ruta",['Selecciona'] + res_busqueda)
        ok = st.button("BUSCAR")
    if select != 'Selecciona' and ok:
        index =  res_busqueda.index(select)
        modal = Modal(key="Demo Key", title='')
        with modal.container():
            st.markdown(f"**:black[{select}]**")
            st.markdown(f":black[Nivel mínimo de la ruta: {minlevel[index]}]")
            st.markdown(f":black[Nivel máximo de la ruta: {maxlevel[index]}]")
            st.markdown(f":black[Forma de captura: {method[index]}]")
            st.markdown(f":black[Chance: {chance[index]}%]")
            

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
