import urllib.request
import json


def info(url):
    with urllib.request.urlopen(url) as f:
        temp = json.loads(f.read().decode())
    lat = []
    lon = []
    des = []
    for x in temp["data"]:
        lat.append(x[8])
        lon.append(x[10])
        des.append(x[5])
    return {
        "latitude": lat,
        "longitude": lon,
        "description": des
    }


def getCounts(url):
    temp = info(url)
    local = dict()
    for x in temp["description"]:
        if x in local.keys():
            local[x] += 1
        else:
            local[x] = 0
    return local


getCounts("https://data.cityofnewyork.us/resource/t4f2-8md7.json")
