import plotly.graph_objects as go
import numpy as np
import json, urllib
from urllib.parse import urlencode
import urllib.request
import googlemaps

# need to calculate shortest path from A to B
# Store route and cost of this path

def code():

    start = "Bridgewater, Sa, Australia"
    finish = "Stirling, SA, Australia"

    url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
                ('origin', start),
                ('destination', finish)
     ))
    with urllib.request.urlopen(url) as ur:
        result = json.load(ur)

    for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
        j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
        print(j)

def main():
    code()


if __name__ == '__main__':
    main()