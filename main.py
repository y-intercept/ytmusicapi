##### WIP #####
import json
import ytmusicapi
import pprint
import tqdm

#Setup Client
ytmusicapi.YTMusic.setup(filepath=r"C:\Documents\CODE\ytmusicapi\headers_auth.json")
yt = ytmusic_client = ytmusicapi.YTMusic("headers_auth.json")

#Import Spotify data
with open(r"C:\Documents\CODE\Data\spotify_data.json", "r", encoding='utf-8') as myfile:
    data = myfile.read()
spotData = json.loads(data)
pprint.pprint(spotData)

#Compile list of artists 
albums = spotData['tracks']
artistSearchQuery = []
for item in albums:
    artistSearchQuery.append(item['artist'])
print("artistSearchQuery")
pprint.pprint(artistSearchQuery)

#remove duplicates
spotArtists = []
for artist in artistSearchQuery:
    if artist not in spotArtists:
        spotArtists.append(artist)
print("spotArtists")
pprint.pprint( spotArtists)

#get subscribed YT artists
ytArtists = []
subscribedArtists = yt.get_library_subscriptions(limit = 50)
for subArtist in subscribedArtists:
    ytArtists.append(subArtist['artist'])
print("ytArtists")
pprint.pprint(ytArtists)

#check if Spotify artist is already subscribed
ytSearchResult = []
for spotArtist in tqdm(spotArtists):
    if spotArtist not in ytArtists:
        search = yt.search(spotArtist)
        ytSearchResult.append(search)
    else:
        pass    
print("search complete")
pprint.pprint(ytSearchResult)

#Select first item from result
browseIDsResult = []
for id in ytSearchResult:
    browseIDsResult.append(id[0])
print("browseIDsResult")
pprint.pprint(browseIDsResult)

#Extract 'browseId'
browseIDs = []
for bID in tqdm(browseIDsResult):
    id = bID.get('browseId')
    if id is None:
        pass
    else:
        browseIDs.append(id)
pprint.pprint(browseIDs)

#Subscribe
errorIds = []
for id in tqdm(browseIDs):
    if "UC" in id:
        yt.subscribe_artists(id)
    else:
        errorIds.append(id)
print(errorIds)    
