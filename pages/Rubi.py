# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:38:19 2023

@author: luigi
"""

import streamlit as st
import base64
import re
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
import buscar as bus
from streamlit_modal import Modal

st.set_page_config(
    page_title="Pokemon Ruby",
    page_icon="🔅"
)

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Ruby</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4c020e26-b4ca-49cd-8174-5c2cb89c8780/dcxoi05-bb06c6c0-47ed-4838-9bcd-85bb0339e9a0.png/v1/fill/w_600,h_320/pokemon_omega_ruby_logo_by_brfa98_dcxoi05-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzIwIiwicGF0aCI6IlwvZlwvNGMwMjBlMjYtYjRjYS00OWNkLTgxNzQtNWMyY2I4OWM4NzgwXC9kY3hvaTA1LWJiMDZjNmMwLTQ3ZWQtNDgzOC05YmNkLTg1YmIwMzM5ZTlhMC5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.t6PWGvqX1YG_r0DVwLGjFc0dPAsvsy7QG8rRoAd3gxs",
            width=550)

pokemon = st.text_input("Introduce the Pokemon you want to search:")

do = False

if pokemon != '':
    try:
        if bus.maps(pokemon, 'ruby') == 'not found':
            st.error("This pokemon can not be found in this generation")
        else:
            bus.maps(pokemon, 'ruby')
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, 'ruby')
            st.success("Found")
            #im1 = cv2.imread('poly.png')
            #im2 = cv2.imread('hoenn.png')
            #st.write(im1.shape)
            #st.write(im2.shape)
            file_ = open("png_to_gif.gif", "rb")
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
        st.error("This Pokemon do not exist")
        
if do: 
    with l3:
        res_busqueda = bus.formatear(res_busqueda, 'ruby')
        select = st.selectbox("Introduce route",['Select'] + res_busqueda)
        ok = st.button("SEARCH")
    if select != 'Select' and ok:
        index =  res_busqueda.index(select)
        modal = Modal(key="Demo Key", title='',max_width='1000px')
        formateado = bus.pinta_ruta(select, "ruby")
        with modal.container():
            x,y,z,x1,y1,z1=st.columns(6)
            with y:
                file_ = open("png_to_gif_pop.gif", "rb")
                contents4 = file_.read()
                data_url4 = base64.b64encode(contents4).decode("utf-8")
                file_.close()
                st.markdown(f'<img src="data:image/gif;base64,{data_url4}" width="450" height="400" alt="gif">',
                                                unsafe_allow_html=True)

            with st.expander("Pokemon info"):
                    st.markdown(f"**:black[{select}]**")
                    st.markdown(f":black[Minime level for this route: {minlevel[index]}]")
                    st.markdown(f":black[Maximum level for this route: {maxlevel[index]}]")
                    st.markdown(f":black[Way of capture: {method[index]}]")
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
