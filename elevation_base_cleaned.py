import requests 
import json  
import pandas as pd
api_key = 

url = "https://maps.googleapis.com/maps/api/elevation/json?locations="


csv_dir =

elev_list = []


def get_elev(x, y):
    json_cord = requests.get(url + str(y) + "," + str(x) + "&key=" + api_key) #api call
    json_data = json_cord.content
    json_file = json.loads(json_data)
    

    for p in json_file["results"]:
        elev = p["elevation"]
        elev = elev * 3.28084
        elev_list.append(elev)

df = pd.read_csv(csv_dir)
x_list = df["Long (wgs84)"].tolist()
y_list = df["Lat (wgs84)"].tolist()
name_list = df["Name"].tolist()

for x,y in zip(x_list, y_list):
    get_elev(x, y)

for elev, name in zip (elev_list, name_list):
    #print("Name: %s Elevation: %s"%(name,elev,))
    print(elev)
