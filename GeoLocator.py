import geocoder
import folium

def printDetails(ip):
    g = geocoder.ip(ip)
    if not g.ok:
        print("Could not find location")
        return

    print(f"IP Address: {ip}")
    print(f"Location: {g.city}, {g.state}, {g.country}")
    print(f"Coordinates: (Lat: {g.latlng[0]}, Lng: {g.latlng[1]})")

    loc = g.latlng
    map = folium.Map(location=loc, zoom_start=10)
    folium.CircleMarker(location=loc, radius=50, color="red").add_to(map)
    folium.Marker(loc).add_to(map)
    map.save("map.html")
    print("Map has been saved as map.html")

ip_add = input("Enter IP: ")
printDetails(ip_add)

