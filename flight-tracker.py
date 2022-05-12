# https://openskynetwork.github.io/opensky-api/rest.html

import requests
import json
import webbrowser
from time import sleep


# print(json.dumps(obj, indent=2))

aircrafts_seen = set()

for i in range(100):
    # set lamin, lomin, lamax, lomax manually in url
    url = "https://opensky-network.org/api/states/all?lamin=40.775001&lomin=-74.020296&lamax=40.879116&lomax=-73.924533"
    response = requests.request("GET", url)
    obj = response.json()
    aircrafts_in_area = []
    if len(obj['states']) == None:
        sleep(1)
        continue
    for j in range(len(obj['states'])):
        icao = obj['states'][j][0]
        aircrafts_seen.add(icao)
        aircrafts_in_area.append(obj['states'][j][0])
    print(f"{str(i + 1).zfill(3)}. Planes currently in area: {aircrafts_in_area}")

    sleep(1)
print(f'Aircrafts seen during runtime: {aircrafts_seen}')

# code below will open a url tracking the current aircraft stored in the variable icao (line 23)

# open_url = f'https://globe.adsbexchange.com/?icao={icao}'
# webbrowser.open(open_url)


