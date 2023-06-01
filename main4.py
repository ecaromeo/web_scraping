import re
import csv
import json
from googleapiclient.discovery import build

api_key = "AIzaSyCTRqXi7x7kgrSeV164FYsnmmE6AQEHiZQ"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_description(video_id):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    return response['items'][0]['snippet']['description']

def get_channel_videos(channel_id):
    videos = []
    next_page_token = None
    while True:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            type='video',
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        videos.extend(response['items'])
        next_page_token = response.get('nextPageToken')
        if next_page_token is None:
            break
    video_dd = []
    for item in videos:
        try:
            video_id = item['id']['videoId']
            video_description = get_video_description(video_id)
            video_dd.append([video_id, video_description])
        except:
            pass

    return video_dd


def extract_links(description):
    return re.findall("(?P<url>https?://[^\s]+)", description)


videos = get_channel_videos("UC4V3oCikXeSqYQr0hBMARwg")

with open('videos.csv', mode='a') as file:
    writer = csv.writer(file)
    # writer.writerow(["Video ID", "Description"])
    for video in videos:
        links = extract_links(video)
        writer.writerow(links)


