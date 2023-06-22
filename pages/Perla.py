import streamlit as st
import base64
import re
from st_pages import Page, show_pages, hide_pages
from streamlit_extras.switch_page_button import switch_page
import buscar as bus
from streamlit_modal import Modal

st.markdown("<h1 style='text-align: center; color: grey;'>Pokemon Perla</h1>", unsafe_allow_html=True)

a,b,c,d,e,f,g,h,i,j = st.columns(10) 

with  b:
    st.image(
           "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4c020e26-b4ca-49cd-8174-5c2cb89c8780/dcxolpc-e1ef145f-2646-450d-9423-c3a88e3d7a5c.png/v1/fill/w_600,h_320/pokemon_pearl_logo_by_brfa98_dcxolpc-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzIwIiwicGF0aCI6IlwvZlwvNGMwMjBlMjYtYjRjYS00OWNkLTgxNzQtNWMyY2I4OWM4NzgwXC9kY3hvbHBjLWUxZWYxNDVmLTI2NDYtNDUwZC05NDIzLWMzYTg4ZTNkN2E1Yy5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.XfVPc2YYOSrSzDvkw_1yjr76Dm8-ZnusTrc6NUKqK5g",
            width=550)

pokemon = st.text_input("Introduce el pokemon que quieres buscar:")

do = False

if pokemon != '':
    try :
        if bus.maps(pokemon, 'pearl') == 'not found':
            st.error("Este pokemon no se encuentra en esta generación")
        else:
            bus.maps(pokemon, 'pearl')
            do = True
            res_busqueda, minlevel, maxlevel, method, chance = bus.locations(pokemon, 'pearl')
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