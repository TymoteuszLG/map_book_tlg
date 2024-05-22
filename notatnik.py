import requests
import folium
from bs4 import BeautifulSoup
from models.data import users



def map_single_users(imie,postow,miasto:str):

    url=(f'https://pl.wikipedia.org/wiki/{miasto}')
    response=requests.get(url)
    response_html=BeautifulSoup(response.text,'html.parser')
    longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    print(longitude,latitude)
    map=folium.Map(location=[latitude,longitude],zoom_start=11)
    folium.Marker(location=[latitude,longitude],popup=f'{imie},postów: {postow},\n{miasto}',icon=folium.Icon(color='blue')).add_to(map)
    map.save(f'map_{miasto}.html')


# for user in users:
#     map_single_users(user['name'],user['post'],user['location'])


def map_all_users(users):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for user in users:

        url = (f'https://pl.wikipedia.org/wiki/{miasto}')
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude], popup=f'{user['name']},postów: {user['location']},\n{miasto}',
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save(f'map_all.html')
map_all_users(users)


