# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:45:40 2023

@author: luigi
"""
import streamlit as st
import base64
import re
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
import buscar as bus
from PIL import Image
from streamlit_modal import Modal

st.set_page_config(
    page_title="Pokemon White",
    page_icon="🔅",
)

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon White</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4c020e26-b4ca-49cd-8174-5c2cb89c8780/dcxom7u-edead424-4a99-4c3a-975b-99126d343dd6.png/v1/fill/w_600,h_320/pokemon_white_logo_by_brfa98_dcxom7u-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzIwIiwicGF0aCI6IlwvZlwvNGMwMjBlMjYtYjRjYS00OWNkLTgxNzQtNWMyY2I4OWM4NzgwXC9kY3hvbTd1LWVkZWFkNDI0LTRhOTktNGMzYS05NzViLTk5MTI2ZDM0M2RkNi5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.6BRIsYp90TWle-Xl8tvHD8Qjxd6pKDJ6lpWt382ojvg",
            width=550)


poke_list=open("./lists/gen5.txt",'r')
poke_list=[i[:-1].lower() for i in poke_list]
pokemon = st.selectbox("Introduce the Pokemon you want to search:",['']+poke_list)


do = False

if pokemon != '':

        if bus.maps(pokemon, 'white') == 'not found':
            st.error("This pokemon can not be found in this generation")
        else:
            bus.maps(pokemon, 'white')
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, 'white')
            st.success("Found")
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
                dim = Image.open("spriteGIF.gif").size
                w = dim[0] * 1.8
                h = dim[1] * 1.8
                st.markdown(f'<img src="data:image/gif;base64,{data_url2}"  width={w} height={h} alt="cat gif">',
                            unsafe_allow_html=True)

                st.write("")
                tipos = bus.get_tipo(pokemon)
                st.image(f"tipos/{tipos[0]}.png")

                bus.get_audio(pokemon)
                audio_file = open('crie.mp3', 'rb')
                audio_bytes = audio_file.read()
                
                st.audio(audio_bytes, format='audio/mp3')
                
                
                

        
if do: 
    with l3:
        res_busqueda = bus.formatear(res_busqueda, 'white')
        select = st.selectbox("Introduce route",['Select'] + res_busqueda)
        ok = st.button("SEARCH")
    if select != 'Select' and ok:
        index =  res_busqueda.index(select)
        modal = Modal(key="Demo Key", title='',max_width='1000px')
        formateado = bus.pinta_ruta(select, "white")
        with modal.container():
            x,y,z,x1,y1,z1=st.columns(6)
            with y:
                file_ = open("pruebaGIF_pop.gif", "rb")
                contents4 = file_.read()
                data_url4 = base64.b64encode(contents4).decode("utf-8")
                file_.close()
                st.markdown(f'<img src="data:image/gif;base64,{data_url4}" width="450" height="400" alt="gif">',
                                                unsafe_allow_html=True)
                st.write("")
            with st.expander("Pokemon info"):
                    st.markdown(f":black[Selected area: {select}]")
                    st.markdown(f":black[Minimum level for this route: {minlevel[index]}]")
                    st.markdown(f":black[Maximum level for this route: {maxlevel[index]}]")
                    st.markdown(f":black[Way of capture: {method[index]}]")
                    st.markdown(f":black[Encounter chance: {chance[index]}%]")

st.write("")
bug = st.button("Report Bug")
if bug:
    modal = Modal(key="Demo Key", title='',max_width='1000px')
    with modal.container():
        bug=st.text_input("What bug did you have?")
        f = open("./bugs/bug.txt", "w")
        f.write(f"{pokemon};white;{bug}\n")
        f.close()


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
