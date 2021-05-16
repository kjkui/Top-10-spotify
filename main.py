import requests, json

def main(playlist_id):
	token = open('token', 'r').read()
	header = {
				"Accept": "application/json",
				"Content-Type": "application/json",
				"Authorization": f"Bearer {token}"
			}
	update = removeTracksFromPlaylist(header, playlist_id)

def getPlaylistItems(header, playlist_id):
	data = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers = header)
	item = data.json()
	respon = json.loads('{"tracks":[]}')
	for i in item["items"]:
		uri = i["track"]["uri"]
		respon["tracks"].append({"uri":  uri})
	print("Get Tracks :)")
	return respon

def updatePlaylist(header, tracklist, playlist_id):
	data = requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={tracklist}', headers = header)
	print(f"Playlist {playlist_id} updated :)")
	return "OK"

def getTop10Tracks(header, playlist_id):
	data = requests.get(f'https://api.spotify.com/v1/me/top/tracks?limit=10&time_range=short_term', headers = header)
	tracklist = ''
	for i in data.json()["items"]:
		tracklist += i["uri"] + ','
	print("Get top 10 :)")
	return updatePlaylist(header, tracklist, playlist_id)

def removeTracksFromPlaylist(header, playlist_id):
	payload = getPlaylistItems(header, playlist_id)
	data = requests.delete(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers = header, data = json.dumps(payload))
	print("deleted :)")
	return getTop10Tracks(header, playlist_id)

main("3dE3k7fQwagwH5ApitMwnz")