import re
import csv
from urllib.parse import urlparse
import requests
import json

def extract_links(description):
    links = re.findall("(?P<url>https?://[^\s]+)", description)
    domains = []
    for link in links:
        try:
            link = requests.head(link).headers['location']
        except:
            pass
        domains.append(urlparse(link).netloc)
    return domains


with open("videos_description.json") as ff:
    videos = json.load(ff)

with open("link_domains.json") as ff:
    domains = json.load(ff)

videos_len = len(videos)
videos = videos[len(domains):]

for _, descr in videos:
    print(f'executing video number {len(domains)+1} out of {videos_len}')
    domains.append(extract_links(descr))

with open('link_domains2.json','w') as ff:
    json.dump(domains, ff)
