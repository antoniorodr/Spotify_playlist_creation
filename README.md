# Spotify playlist creation

This script creates a Spotify playlist with the top 100 songs from the date you choose. You will need to create an Spotify app from [here](https://developer.spotify.com).

Choose the name you want and "Web API". Once created, copy the client ID and client secret into a .env file.

Use "http://example.com" as the redirect URL in your app.

The first time you run the script, it will ask you to paste the url you were redirected to. Do it and click enter. It will create then a token.txt file and you can run the script again.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SPOTIPY_CLIENT_ID`="Your_client_ID"

`SPOTIPY_CLIENT_SECRET`="Your_client_secret"

`SPOTIPY_REDIRECT_URI`="http://example.com"

`SPOTIFY_NAME`="Your_spotify_account_name"
