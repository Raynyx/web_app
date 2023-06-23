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

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Negro</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4c020e26-b4ca-49cd-8174-5c2cb89c8780/dcxom75-e1944a3d-0511-407a-9b2b-8108e3030d21.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzRjMDIwZTI2LWI0Y2EtNDljZC04MTc0LTVjMmNiODljODc4MFwvZGN4b203NS1lMTk0NGEzZC0wNTExLTQwN2EtOWIyYi04MTA4ZTMwMzBkMjEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.ERtmSmhxdofBxHdA0pRdy1bJe_ZO99-hpp8Wv9RNXso",
            width=550)

pokemon = st.text_input("Introduce el pokemon que quieres buscar:")

do = False

if pokemon != '':
    try :
        if bus.maps(pokemon, 'black') == 'not found':
            st.error("Este pokemon no se encuentra en esta generación")
        else:
            bus.maps(pokemon, 'black')
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, 'black')
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
            with l:
                st.write("              ")

            
            with l3:
                bus.get_sprite(pokemon)
                file_ = open("spriteGIF.gif", "rb")
                contents2 = file_.read()
                data_url2 = base64.b64encode(contents2).decode("utf-8")
                file_.close()
                st.markdown(f'<img src="data:image/gif;base64,{data_url2}"  width="150" height="150" alt="cat gif">',
                            unsafe_allow_html=True)

                st.write("")
                tipos = bus.get_tipo(pokemon)
                for tipo in tipos:
                    path = f"tipos/{tipo}.png"
                    st.image(path)

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
    modal = Modal(key="Demo Key", title='',max_width='1000px')
    formateado = bus.pinta_ruta(select, "black")
    st.write(formateado)
    with modal.container():
        x,y,z=st.columns(3)
        with x:
            file_ = open("pruebaGIF_pop.gif", "rb")
            contents4 = file_.read()
            data_url4 = base64.b64encode(contents4).decode("utf-8")
            file_.close()
            st.markdown(f'<img src="data:image/gif;base64,{data_url4}" width="600" height="600" alt="gif">',
                                            unsafe_allow_html=True)
        with st.expander("Pokemon info"):
                st.markdown(f"**:black[{select}]**")
                st.markdown(f":black[Nivel mínimo de la ruta: {minlevel[index]}]")
                st.markdown(f":black[Nivel máximo de la ruta: {maxlevel[index]}]")
                st.markdown(f":black[Forma de captura: {method[index]}]")
                st.markdown(f":black[Chance: {chance[index]}%]")

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
