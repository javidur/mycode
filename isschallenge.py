#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

url = "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(url).json()
    
    # viewing the response
    print(resp)
    
    # capturing lat and long
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]

    # converting timestamp to date-time
    timestamp = resp["timestamp"]
    date_time = datetime.datetime.fromtimestamp(timestamp)
    
    # rg must be passed a tuple 
    coords = (lat, lon)
    result = rg.search(coords)
    city = result[0]["name"]
    country = result[0]["cc"]

    # printing timestamp, lat, and long
    print(f"""CURRENT LOCATION OF THE ISS:
    Timestamp: {date_time}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}""")

if __name__ ==  "__main__":
    main()
