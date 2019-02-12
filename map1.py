import folium
import pandas

data = pandas.read_csv("volcal.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation < 3000:
        return 'orange'
    else:
        return 'red'

#html1
# html = """<h4>Volcano information:</h4>
# Height: %s m
# """

#html2
name = list(data["NAME"])
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg_volcano = folium.FeatureGroup(name="My Map")


#html1
# for lt, ln, el in zip(lat, lon, elev):
#     iframe = folium.IFrame(html=html % str(el), width=200, height=100)
#     fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

#html2
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg_volcano.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), fill_opacity=0.7, color="grey", fill_color=color_producer(el) ))

fg_population = folium.FeatureGroup(name="My Map")
  
fg_population.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {'fillColor':'yellow' 
    if x['properties']['POP2005'] < 10000000 
    else 'orange'
    if 1000000 <= x['properties']['POP2005'] < 20000000 
    else 'red'}))
    
map.add_child(fg_volcano)
map.add_child(fg_population)
map.add_child(folium.LayerControl())


map.save("map1.html")