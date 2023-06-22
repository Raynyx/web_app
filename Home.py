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
            "https://static.wikia.nocookie.net/nintendo/images/5/59/Pokemon_Red_%28NA%29.png/revision/latest?cb=20120331144754&path-prefix=en",
            "https://archives.bulbagarden.net/media/upload/thumb/5/5a/Blue_EN_boxart.png/250px-Blue_EN_boxart.png",
            "https://static.wikia.nocookie.net/pokemon/images/a/a5/Pokemon_Yellow.jpg/revision/latest?cb=20200620223058"
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
