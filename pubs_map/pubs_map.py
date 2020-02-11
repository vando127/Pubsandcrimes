import pandas
import folium

data = pandas.read_csv("2019-08-city-of-london-street.csv")[0:820]
datamet = pandas.read_csv("2019-08-metropolitan-street.csv")[0:90447]

lat = list(data["Latitude"])
lon = list(data["Longitude"])
latmet = list(datamet["Latitude"])
lonmet = list(datamet["Longitude"])


map = folium.Map(location =[51.5163776, -0.1620758], zoom_start = 12, titles="Stamen Terrain")

fgc = folium.FeatureGroup(name = "City Police")


for lt, ln in zip(lat, lon):
    fgc.add_child(folium.CircleMarker(location =[lt, ln], color = "red", fill_color = "red", fill_opacity = 0.6, radius=1))

fgm = folium.FeatureGroup(name = "Met. Police")

for lt1, ln1 in zip(latmet, lonmet):
    fgm.add_child(folium.CircleMarker(location =[lt1, ln1], color = "red", fill_color = "red", fill_opacity = 0.6, radius=1))

#fgpdata = pandas.read_json("londonpubs.json")

fgp = folium.FeatureGroup(name = " Pubs ")
#fga = folium.FeatureGroup(name = " Pubs ")

#styling icon with given surronding crimes - MISSING#
fgp.add_child(folium.GeoJson(data=open('londonpubs.json','r', encoding='utf-8-sig').read(),
tooltip = folium.features.GeoJsonTooltip(['name'], label=False)))


map.add_child(fgc)
map.add_child(fgm)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("PubsMaps.html")
