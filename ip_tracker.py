#!/usr/bin/env python3
# made by https://github.com/EyuCoder
import argparse
import requests
import json
import sys, time


base_url = 'https://geo.leadboxer.com/GeoIpEngine/'

parser = argparse.ArgumentParser()
parser.add_argument ("-t", dest='target', help= "target's ip-address", type=str, required=False )

args = parser.parse_args()

ip = args.target if args.target else ''

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def banner():
    
    print(OKGREEN +
'''
 ██▓ ██▓███     ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░░            ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
'''
)

def printer(data):
    print(BOLD + OKCYAN + 
f'''
────────────────────────────────────────────────────────────────────────────
date:               {data["date"]},
ip address:         {data["ip"]},
ip range:           {data["ip range"]},
countryCode:        {data["countryCode"]},
countryName:        {data["countryName"]},
city:               {data["city"]},
continent:          {data["continent"]},
subContinent:       {data["subContinent"]},
Geolocation:        https://www.google.com/maps/?q={data["latitude"]},{data["longitude"]}
latitude:           {data["latitude"]},
longitude:          {data["longitude"]},
timezone:           {data["timezone"]},
offset:             {data["offset"]},
────────────────────────────────────────────────────────────────────────────
org:                {data["org"]},
isp:                {data["isp"]},
domain:             {data["domain"]},
usageType:          {data["usageType"]},
mm_org:             {data["mm_org"]},
mm_isp:             {data["mm_isp"]},
i2l_isp:            {data["i2l_isp"]},
i2l_domain:         {data["i2l_domain"]},
i2l_type:           {data["i2l_type"]}
────────────────────────────────────────────────────────────────────────────
region:             {data["region"]},
regionName:         {data["regionName"]},
surfaceArea:        {data["surfaceArea"]},
population:         {data["population"]},
lifeExpectency:     {data["lifeExpectency"]},
GNP:                {data["GNP"]},
world currency:     {data["world currency"]},
EU member:          {data["EU member"]},
────────────────────────────────────────────────────────────────────────────
'''
            )


banner()

try:
    response = requests.get(base_url + ip + '?jsonp')
    data = response.json()
    printer(data)

except requests.exceptions.Timeout as e:
    print(f'request timeout: {e}')
except requests.exceptions.TooManyRedirects as e:
    print(f'bad url: {e}')
except requests.exceptions.RequestException as e:
    print(f'fatal error: {e}')
    raise SystemExit(e)
