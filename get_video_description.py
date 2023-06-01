import re
import csv
import json
from googleapiclient.discovery import build

api_key = "AIzaSyCTRqXi7x7kgrSeV164FYsnmmE6AQEHiZQ"
youtube = build('youtube', 'v3', developerKey=api_key)
with open("videos.json") as ff:
    videos = json.load(ff)

def get_video_description(video_id):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    return response['items'][0]['snippet']['description']

video_dd = []

for item in videos:
    try:
        video_id = item
        video_description = get_video_description(video_id)
        video_dd.append([video_id, video_description])
    except:
        pass

with open('videos_description.json','w') as ff:
    json.dump(video_dd, ff)