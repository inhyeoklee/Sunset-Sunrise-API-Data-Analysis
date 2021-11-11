#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 13:14:21 2021

@author: inhyeoklee
"""

import requests
import csv
import json

csv_file = open('sunrise_sunset_austin.csv', 'w')
# file_out = 'sunrise_sunset_austin.csv'
url = 'https://api.sunrise-sunset.org/json?lat=30.267153&lng=-97.743057'
city = 'austin'
year = '2021'

res = requests.get(url)
resJson = json.loads(res.text)
data = resJson['results']
sunrise = data["sunrise"]
print(sunrise)
sunset = data["sunset"]
print(sunset)
solar_noon = data["solar_noon"]

csv_file.write("sunrise:"+sunrise+"\n")
csv_file.write("sunset:"+sunset+"\n")
csv_file.close()