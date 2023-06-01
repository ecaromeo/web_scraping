import re
import csv
import json
from googleapiclient.discovery import build

api_key = "AIzaSyCTRqXi7x7kgrSeV164FYsnmmE6AQEHiZQ"
youtube = build('youtube', 'v3', developerKey=api_key)


response = youtube.channels().list(
    id = "UC4V3oCikXeSqYQr0hBMARwg",
    part = 'contentDetails',
    fields = 'items(contentDetails(relatedPlaylists(uploads)))',
    maxResults = 1
).execute()

UPLOADS_ID = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


is_video = lambda item: \
    item['snippet']['resourceId']['kind'] == 'youtube#video'
video_id = lambda item: \
    item['snippet']['resourceId']['videoId']

request = youtube.playlistItems().list(
    playlistId = UPLOADS_ID,
    part = 'snippet',
    fields = 'nextPageToken,items(snippet(resourceId))',
    maxResults = 50
)
videos = []

while request:
    response = request.execute()

    items = response.get('items', [])

    videos.extend(map(video_id, filter(is_video, items)))

    request = youtube.playlistItems().list_next(
        request, response)
    
with open('videos.json','w') as ff:
    json.dump(videos, ff)