# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:32:52 2023

@author: luigi
"""

import streamlit as st
import base64
from st_clickable_images import clickable_images
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal

st.markdown("<h1 style='text-align: center; color: grey;'>Buscador de Pokemon</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>¿Quieres saber donde encontrar un pokemón?</h3>", unsafe_allow_html=True)

st.markdown("<text style='text-align: center; color: black;'>Pokemon siempre a sido uno de los juegos que mayor número de jugadores a tenido. Por lo que cada vez hay más jugadores nuevos y no sabe donde pueden buscar un pokemon que quieren. Por ello usando este app será mucho más fácil. </text>", unsafe_allow_html=True)

file_ = open("Pikachu.gif", "rb")
file_2 = open("Pikachu2.gif", "rb")
contents1 = file_.read()
contents2 = file_2.read()
data_url1 = base64.b64encode(contents1).decode("utf-8")
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_.close()
file_2.close()
_left, _right = st.columns(2)
with _left:
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url1}"  width="250" height="250" alt="cat gif">',
    unsafe_allow_html=True)
with _right:
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url2}"  width="250" height="250" alt="cat gif">',
    unsafe_allow_html=True)

gen = st.selectbox("Seleccionar generación: ", ["GEN-1","GEN-2","GEN-3","GEN-4","GEN-5"])

if gen == 'GEN-1':
    clicked = clickable_images(
        [
            "data:image/jpeg;base64,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",
            "https://archives.bulbagarden.net/media/upload/thumb/5/5a/Blue_EN_boxart.png/250px-Blue_EN_boxart.png",
            "https://static.wikia.nocookie.net/pokemon/images/a/a5/Pokemon_Yellow.jpg/revision/latest/scale-to-width-down/350?cb=20200620223058"
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )
    
    if clicked == 0:
        st.write("Buscando en el juego de Pokemon Rojo")
        switch_page('Red')
    elif clicked == 1:
        st.write("Buscando en el juego de Pokemon Azul")
        switch_page('Blue')
    elif clicked == 2:
        st.write("Buscando en el juego de Pokemon Amarillo")
        switch_page('Yellow')
        
if gen == 'GEN-2':
    clicked = clickable_images(
        [
            "https://images.wikidexcdn.net/mwuploads/wikidex/d/dd/latest/20190811004250/Logo_Serie_Oro_y_Plata.png",
            "https://www.pokebip.com/pages/jeuxvideo/logos/cristal.png",
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "180px"},
    )
    
    if clicked == 0:
        st.write("Buscando en el juego de Pokemon Oro y Plata")
        switch_page('OyP')
    elif clicked == 1:
        st.write("Buscando en el juego de Pokemon Cristal")
        switch_page('Cristal')
        
if gen == 'GEN-3':
    clicked = clickable_images(
        [
            "https://upload.wikimedia.org/wikipedia/commons/3/35/Pok%C3%A9mon_Ruby_%26_Sapphire_Logos.png",
            "https://cutewallpaper.org/24/pokemon-emerald-png/31-pokemon-emerald-logo-transparent-icon-logo-design.png",
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "280px"},
    )
    
    if clicked == 0:
        st.write("Buscando en el juego de Pokemon Rubí y Zafiro")
        switch_page('RyZ')
    elif clicked == 1:
        st.write("Buscando en el juego de Pokemon Esmeralda")
        switch_page('Esmera')
        
if gen == 'GEN-4':
    clicked = clickable_images(
        [
            "https://cdn.atomix.vg/wp-content/uploads/2014/03/Pokemon-Diamond-Pearl.png",
            "https://upload.wikimedia.org/wikipedia/commons/d/d7/Pokemon_Platinum_Version_logo.png",
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "180px","width":"330px"},
    )
    
    if clicked == 0:
        st.write("Buscando en el juego de Pokemon Diamante y Perla")
        switch_page('DyP')
    elif clicked == 1:
        st.write("Buscando en el juego de Pokemon Platino")
        switch_page('Platino')
        
if gen == 'GEN-5':
    clicked = clickable_images(
        [
            "https://assets.pokemon.com/assets/cms2-es-es/img/watch-pokemon-tv/seasons/season14/season14_logo_169_es.jpg",
            "https://www.nintenderos.com/wp-content/uploads/2012/06/pokemon-blanco-2-nintendo-ds.png?width=1200&enable=upscale",
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )
    
    if clicked == 0:
        st.write("Buscando en el juego de Pokemon Negro y Blanco")
        switch_page('NyB')
    elif clicked == 1:
        st.write("Buscando en el juego de Pokemon Negro 2 y Blanco 2")
        switch_page('NyB2')
    
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

if st.button("*Boton oculto*"):
    modal = Modal(key="Demo Key", title='')
    with modal.container():
        st.markdown('No hay nada XD')
