import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/1196941328/playlists'
ACCESS_TOKEN = 'BQC7DPGv4-wOB5THxPS0ejeAX7AX6_Ien1IvEgCr396s4hNjNfJlXfu_DULoQIuq1iVVqR2BhwjN8Ppcoi-toLl-8lUMYAZbe8czT1019rvOyPB9HCJiV79EVPkZANEL3OMlXaWEerSU1eZOOSfcLwsXrVlxLgL2EZFwLfaiQpFLQlUxHiaWTlQvphrxHiQcZBvEIeyf1-pPDXKYTKFyHzv03TVgzCvVax8AOBGvTbdc'

def create_playlist(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist(
        name="My Private Playlist",
        public=False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()