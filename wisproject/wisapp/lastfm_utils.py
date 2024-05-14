# lastfm_utils.py
import requests
from django.conf import settings

def get_top_tracks_by_artists(artists):
    api_key = settings.LASTFM_API_KEY
    top_tracks = []

    for artist in artists:
        url = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={api_key}&format=json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for track in data['toptracks']['track'][:2]:
                top_tracks.append({
                    'artist': artist,
                    'name': track['name'],
                    'playcount': track['playcount'],
                    'listeners': track['listeners'],
                    'url': track['url']
                })
        else:
            print(f"Error fetching top tracks for {artist}: {response.status_code}, {response.text}")

    return top_tracks
