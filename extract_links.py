import re
import csv
from urllib.parse import urlparse
import requests
import json

def extract_links(description):
    links = re.findall("(?P<url>https?://[^\s]+)", description)
    domains = []
    for link in links:
        domains.append(link)
    return domains


with open("videos_description.json") as ff:
    videos = json.load(ff)

videos_len = len(videos)
domains = []

for id, descr in videos:
    print(f'executing video number {len(domains)+1} out of {videos_len}')
    domains.append([id, extract_links(descr)])

with open('extracted_links.json','w') as ff:
    json.dump(domains, ff)
