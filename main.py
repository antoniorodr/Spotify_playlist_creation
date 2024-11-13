import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# URL = f"https://www.billboard.com/charts/hot-100/{user_input}/"
URL = "https://www.billboard.com/charts/hot-100/2024-08-03/"


response = requests.get(URL, headers = header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="SPOTIPY_REDIRECT_URI=",
        client_id="SPOTIPY_CLIENT_ID",
        client_secret="SPOTIPY_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="SPOTIFY_NAME",
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#FIX: Illegal URL

# scope = "user-library-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
