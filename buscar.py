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
    juegos = {"black":"teselia","white":"teselia","white-2":"teselia", "black-2":"teselia","pearl":"sinnoh",
             "diamond":"sinnoh","platinum":"sinnoh", "red":"kanto","blue":"kanto"}
    region = juegos[juego]
    
    res_busqueda, minlevel, maxlevel, method, chance = locations(pokemon, juego)

    if len(res_busqueda) == 0:
        return "not found"
    
    sinnoh, teselia, kanto = False, False, False
    if region == "teselia":
        teselia = True
    elif region == "sinnoh":
        sinnoh = True
    elif region == "kanto":
        kanto = True
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
                    image = cv2.fillPoly(image, [pt], (255,0,0))
                elif "bridge" in i["label"]:
                    pt = diag(i["points"])
                    pt = np.array(pt, np.int32)
                    image = cv2.fillPoly(image, [pt], (255,0,0))
                else:
                    radio = abs(i["points"][0][0] - i["points"][1][0]) + abs(i["points"][0][1] - i["points"][1][1])
                    center = (int(i["points"][0][0]),int(i["points"][0][1]))
                    image = cv2.circle(image, center, int(radio), (0,0,255), thickness = 3)
            elif sinnoh:
                pt = diag(i["points"])
                pt = np.array(pt, np.int32)
                image = cv2.fillPoly(image, [pt], (255,0,0))

    cv2.imwrite(r"poly.png",image)
    
    images = []
    for filename in [f"{region}.png","poly.png"]:
        images.append(iio.imread(filename))
                
    iio.mimwrite(uri="pruebaGIF.gif",ims=images,loop=0, duration = 1000)

def pinta_ruta(route, juego):
    
    juegos = {"black":"teselia","white":"teselia","white-2":"teselia", "black-2":"teselia","pearl":"sinnoh",
             "diamond":"sinnoh","platinum":"sinnoh", "red":"kanto","blue":"kanto"}
    region = juegos[juego]
    
    imdata = base64.b64decode(data["imageData"])
    npimg = np.frombuffer(imdata, dtype=np.uint8);
    im0 = cv2.imdecode(npimg, 1)

    image = im0
    for i in data["shapes"]:
        if i["label"] == route:
            if teselia:
                if "route" in i["label"]:
                    pt = np.array(i["points"], np.int32)
                    image = cv2.fillPoly(image, [pt], (255,0,0))
                elif "bridge" in i["label"]:
                    pt = diag(i["points"])
                    pt = np.array(pt, np.int32)
                    image = cv2.fillPoly(image, [pt], (255,0,0))
                else:
                    radio = abs(i["points"][0][0] - i["points"][1][0]) + abs(i["points"][0][1] - i["points"][1][1])
                    center = (int(i["points"][0][0]),int(i["points"][0][1]))
                    image = cv2.circle(image, center, int(radio), (0,0,255), thickness = 3)
            elif sinnoh:
                pt = diag(i["points"])
                pt = np.array(pt, np.int32)
                image = cv2.fillPoly(image, [pt], (255,0,0))
                
    cv2.imwrite(r"poly_pop.png",image)
    
    images = []
    for filename in [f"{region}.png","poly_pop.png"]:
        images.append(iio.imread(filename))
                
    iio.mimwrite(uri="pruebaGIF_pop.gif",ims=images,loop=0, duration = 1000)
