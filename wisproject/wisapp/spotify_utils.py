import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

def get_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def fetch_latest_releases_by_artists(artist_names):
    spotify = get_spotify_client()
    releases = []
    for name in artist_names:
        artist_search = spotify.search(q='artist:' + name, type='artist', limit=1)
        if artist_search['artists']['items']:
            artist_id = artist_search['artists']['items'][0]['id']
            artist_albums = spotify.artist_albums(artist_id, album_type='single', country='US', limit=1, offset=0)
            if artist_albums['items']:
                recent_album = artist_albums['items'][0]
                album_tracks = spotify.album_tracks(recent_album['id'], limit=1)
                if album_tracks['items']:
                    track = album_tracks['items'][0]
                    releases.append({
                        'name': track['name'],
                        'artist': name,
                        'release_date': recent_album['release_date'],
                        'cover_url': recent_album['images'][0]['url'] if recent_album['images'] else None,
                        'spotify_url': track['external_urls']['spotify']
                    })
    return releases
