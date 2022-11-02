#!/usr/bin/env python3

import argparse
import requests
import json


base_url = 'https://geo.leadboxer.com/GeoIpEngine/'

parser = argparse.ArgumentParser()
parser.add_argument ("-t", dest='target', help= "target's ip-address", type=str, required=False )

args = parser.parse_args()

ip = args.target if args.target else ''

def printer(data):
    print(
'''

 ___   _______    _______  ______    _______  _______  ___   _  _______  ______   
 |   | |       |  |       ||    _ |  |   _   ||       ||   | | ||       ||    _ |  
 |   | |    _  |  |_     _||   | ||  |  |_|  ||       ||   |_| ||    ___||   | ||  
 |   | |   |_| |    |   |  |   |_||_ |       ||       ||      _||   |___ |   |_||_ 
 |   | |    ___|    |   |  |    __  ||       ||      _||     |_ |    ___||    __  |
 |   | |   |        |   |  |   |  | ||   _   ||     |_ |    _  ||   |___ |   |  | |
 |___| |___|        |___|  |___|  |_||__| |__||_______||___| |_||_______||___|  |_|

'''
            )
    print(
f'''
date:           {data["date"]},
ip address:     {data["ip"]},
ip range:       {data["ip range"]},
countryCode:    {data["countryCode"]},
continent:      {data["continent"]},
subContinent:   {data["subContinent"]},
surfaceArea:    {data["surfaceArea"]},
population:     {data["population"]},
lifeExpectency: {data["lifeExpectency"]},
GNP:            {data["GNP"]},
countryName:    {data["countryName"]},
region:         {data["region"]},
regionName:     {data["regionName"]},
city:           {data["city"]},
latitude:       {data["latitude"]},
longitude:      {data["longitude"]},
timezone:       {data["timezone"]},
offset:         {data["timezone"]},
world currency: {data["world currency"]},
EU member:      {data["EU member"]},
org:            {data["org"]},
isp:            {data["isp"]},
domain:         {data["domain"]},
usageType:      {data["usageType"]},
mm_org:         {data["mm_org"]},
mm_isp:         {data["mm_isp"]},
i2l_isp:        {data["i2l_isp"]},
i2l_domain:     {data["i2l_domain"]},
i2l_type:       {data["i2l_type"]}
'''
            )

try:
    response = requests.get(base_url + ip + '?jsonp')
    data = response.json()
    print(response)
    printer(data)

except requests.exceptions.Timeout as e:
    print(f'request timeout: {e}')
except requests.exceptions.TooManyRedirects as e:
    print(f'bad url: {e}')
except requests.exceptions.RequestException as e:
    print(f'fatal error: {e}')
    raise SystemExit(e)

