# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:52:55 2023

@author: luigi
"""

import json
import requests as r
import cv2
import base64
import numpy as np
import imageio as iio
import re
from PIL import Image

def locations(pokemon, juego):
    resp = r.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    json_res = json.loads(resp.content)
    url_encounters = json_res["location_area_encounters"]
    res = r.get(url_encounters)
    encounters = json.loads(res.content)
    ###
    results = []
    minlevel = []
    maxlevel = []
    method = []
    chance = []
    for i in encounters:
        for x in i["version_details"]:
            version = x["version"]["name"]
            if version == juego:
                results.append(i["location_area"]["name"])
                minim, maxim = 100,0
                for w in x["encounter_details"]:
                    if w["min_level"] < minim: minim = w["min_level"]
                    if w["max_level"] > maxim: maxim = w["max_level"]
                minlevel.append(minim)
                maxlevel.append(maxim)
                chance.append(x["encounter_details"][0]["chance"])
                method.append(x["encounter_details"][0]["method"]["name"])
    return results, minlevel, maxlevel, method, chance

def diag(punto):
    res = []
    res.append(punto[0])
    res.append([punto[0][0],punto[1][1]])
    res.append(punto[1])
    res.append([punto[1][0],punto[0][1]])
    return res

def maps(pokemon, juego):
    color = (160,255,0)
    juegos = {"black":"teselia","white":"teselia","pearl":"sinnoh",
             "diamond":"sinnoh","platinum":"sinnoh", "red":"kanto","blue":"kanto","yellow":"kanto", 
              "gold":"jhoto", "silver":"jhoto","crystal":"jhoto",
             "ruby":"hoenn", "sapphire":"hoenn","emerald":"hoenn"}
    region = juegos[juego]
    
    res_busqueda, minlevel, maxlevel, method, chance = locations(pokemon, juego)

    if len(res_busqueda) == 0:
        return "not found"
    
    sinnoh, teselia, kanto, jhoto, hoenn = False, False, False, False, False
    if region == "teselia":
        teselia = True
    elif region == "sinnoh":
        sinnoh = True
    elif region == "kanto":
        kanto = True
    elif region == "jhoto":
        jhoto = True
    elif region == "hoenn":
        hoenn = True
    f = open(f"{region}_json.json")
    data = json.load(f)
    
    lugares = set()
    for lugar in data["shapes"]:
        lugares.add(lugar["label"])
    
    formateado = set()
    for res_lugar in res_busqueda:
        try:
            numero = re.findall("\d+",res_lugar)
            for lugar in lugares:
                patron = r"\b" + re.escape(numero) + r"\b"
                if lugar in res_lugar and re.search(patron, lugar):
                    formateado.add(lugar)
        except:
            for lugar in lugares:
                if lugar in res_lugar:
                    formateado.add(lugar)

    imdata = base64.b64decode(data["imageData"])
    npimg = np.frombuffer(imdata, dtype=np.uint8);
    im0 = cv2.imdecode(npimg, 1)
    
    image = im0
    for i in data["shapes"]:
        if i["label"] in formateado:
            if teselia:
                if "route" in i["label"]:
                    pt = np.array(i["points"], np.int32)
                    image = cv2.fillPoly(image, [pt], color)
                elif "bridge" in i["label"]:
                    pt = diag(i["points"])
                    pt = np.array(pt, np.int32)
                    image = cv2.fillPoly(image, [pt], color)
                else:
                    radio = abs(i["points"][0][0] - i["points"][1][0]) + abs(i["points"][0][1] - i["points"][1][1])
                    center = (int(i["points"][0][0]),int(i["points"][0][1]))
                    image = cv2.circle(image, center, int(radio), color, thickness = 3)
            elif sinnoh or kanto or jhoto or hoenn:
                pt = diag(i["points"])
                pt = np.array(pt, np.int32)
                image = cv2.fillPoly(image, [pt], color)

    cv2.imwrite(r"poly.png",image)
    
    images = []
    for filename in [f"{region}.png","poly.png"]:
        if '.png' in filename:
            images.append(iio.imread(filename))
    if region != 'hoenn':
        iio.mimwrite(uri="pruebaGIF.gif",ims=images,loop=0, duration = 1000)
    else:
        frames = []
        for i in [f"{region}.png","poly.png"]:
            new_frame = Image.open(i)
            frames.append(new_frame)

        frames[0].save('png_to_gif.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=300, loop=0)



def pinta_ruta(route, juego):
    color = (160,255,0)
    juegos = {"black":"teselia","white":"teselia","pearl":"sinnoh",
             "diamond":"sinnoh","platinum":"sinnoh", "red":"kanto","blue":"kanto","yellow":"kanto",
             "gold":"jhoto", "silver":"jhoto","crystal":"jhoto",
             "ruby":"hoenn", "sapphire":"hoenn","emerald":"hoenn"}
    region = juegos[juego]
    
    sinnoh, teselia, kanto, jhoto, hoenn = False, False, False, False, False
    if region == "teselia":
        teselia = True
    elif region == "sinnoh":
        sinnoh = True
    elif region == "kanto":
        kanto = True
    elif region == "jhoto":
        jhoto = True
    elif region == "hoenn":
        hoenn = True
    f = open(f"{region}_json.json")
    data = json.load(f)

    imdata = base64.b64decode(data["imageData"])
    npimg = np.frombuffer(imdata, dtype=np.uint8);
    im0 = cv2.imdecode(npimg, 1)

    lugares = set()
    for lugar in data["shapes"]:
        lugares.add(lugar["label"])
        
    formateado = route.replace(' ','-')
                
    image = im0
    for i in data["shapes"]:
        if i["label"] == formateado:
            if teselia:
                if "route" in i["label"]:
                    pt = np.array(i["points"], np.int32)
                    image = cv2.fillPoly(image, [pt], color)
                elif "bridge" in i["label"]:
                    pt = diag(i["points"])
                    pt = np.array(pt, np.int32)
                    image = cv2.fillPoly(image, [pt], color)
                else:
                    radio = abs(i["points"][0][0] - i["points"][1][0]) + abs(i["points"][0][1] - i["points"][1][1])
                    center = (int(i["points"][0][0]),int(i["points"][0][1]))
                    image = cv2.circle(image, center, int(radio), color, thickness = 3)
            elif sinnoh or kanto or jhoto or hoenn:
                pt = diag(i["points"])
                pt = np.array(pt, np.int32)
                image = cv2.fillPoly(image, [pt], color)
                
    cv2.imwrite(r"poly_pop.png",image)
    
    images = []
    for filename in [f"{region}.png","poly_pop.png"]:
        images.append(iio.imread(filename))
                
    if region != "hoenn":
        iio.mimwrite(uri="pruebaGIF_pop.gif",ims=images,loop=0, duration = 1000)
    else:
        frames_pop = []
        for i in [f"{region}.png","poly_pop.png"]:
            new_frame_pop = Image.open(i)
            frames_pop.append(new_frame_pop)

        frames_pop[0].save('png_to_gif_pop.gif', format='GIF',
                   append_images=frames_pop[1:],
                   save_all=True,
                   duration=300, loop=0)

    return formateado

def formatear(res_busqueda, juego):
    juegos = {"black":"teselia","white":"teselia","pearl":"sinnoh",
             "diamond":"sinnoh","platinum":"sinnoh", "red":"kanto","blue":"kanto","yellow":"kanto",
             "gold":"jhoto", "silver":"jhoto","crystal":"jhoto",
             "ruby":"hoenn", "sapphire":"hoenn","emerald":"hoenn"}
    region = juegos[juego]
    
    sinnoh, teselia, kanto, jhoto, hoenn = False, False, False, False, False
    if region == "teselia":
        teselia = True
    elif region == "sinnoh":
        sinnoh = True
    elif region == "kanto":
        kanto = True
    elif region == "jhoto":
        jhoto = True
    elif region == "hoenn":
        hoenn = True
    f = open(f"{region}_json.json")
    data = json.load(f)
    
    lugares = set()
    for lugar in data["shapes"]:
        lugares.add(lugar["label"])
    
    formateado = set()
    for res_lugar in res_busqueda:
        try:
            numero = re.findall("\d+",res_lugar)
            for lugar in lugares:
                patron = r"\b" + re.escape(numero) + r"\b"
                if lugar in res_lugar and re.search(patron, lugar):
                    formateado.add(lugar)
        except:
            for lugar in lugares:
                if lugar in res_lugar:
                    formateado.add(lugar)

    formateado_Final = []
    for route in formateado:
        route_F = route.replace('-', ' ')
        formateado_Final.append(route_F)
    return list(formateado_Final)

def get_sprite(pokemon):
    url = f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif"
    response = r.get(url)

    with open("spriteGIF.gif","wb") as f:
        f.write(response.content)

def get_audio(pokemon):
    url = f'https://play.pokemonshowdown.com/audio/cries/{pokemon}.mp3'
    resp = r.get(url, allow_redirects=True)
    open('crie.mp3', 'wb').write(resp.content)

def get_tipo(pokemon):
    tipos = []
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    resp = r.get(url)
    result = json.loads(resp.content)
    res_tipos = result["types"]
    tipos.append(res_tipos[0]["type"]["name"])
    if len(res_tipos) == 2:
        tipos.append(res_tipos[1]["type"]["name"])
    return tipos
