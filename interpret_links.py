import re
import csv
from urllib.parse import urlparse
import requests
import json
import requests
from bs4 import BeautifulSoup

def resolve_bitly_links(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        resolved_link = soup.find('meta', property='og:url')
        if resolved_link:
            resolved_link = resolved_link['content']
        else:
            resolved_link = None
    else:
        resolved_link = None

    return resolved_link


def interpret_links(inlinks):
    domains = []
    for link in inlinks:
        domain = urlparse(link).netloc
        if "bit.ly" in domain:
            full_link = resolve_bitly_links(link)
            domain = urlparse(full_link).netloc
        elif "bitly" in domain:
            full_link = resolve_bitly_links(link)
            domain = urlparse(full_link).netloc
        elif "tinyurl" in domain:
            full_link = resolve_bitly_links(link)
            domain = urlparse(full_link).netloc
        else:
            domains.append(domain)

    return domains


with open("extracted_links.json") as ff:
    videos = json.load(ff)

videos_len = len(videos)
domains = []
for id, links in videos:
    print(f'executing video number {len(domains)+1} out of {videos_len}')
    domains.append([id, links, interpret_links(links)])

with open('interpreted_links.json', 'w') as ff:
    json.dump(domains, ff)
