import urllib.request
import json


def info(a):
    c = urllib.request.urlopen(a)
    d = c.read().decode()
    c = json.loads(d)
    data = []
    for line in c:
        if "latitude" in line.keys():
            if "longitude" in line.keys():
                data.append([float(line["latitude"]), float(line["longitude"]), line["boro_name"]])
    return json.dumps(data)
