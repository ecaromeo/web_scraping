import re
import csv
from urllib.parse import urlparse
import requests
import json

#TODO
def interpret_links(inlinks):
    domains = []
    for link in inlinks:
        domain = urlparse(link).netloc
        if "bit.ly" in domain:
            pass
        elif "bitly" in domain:
            pass
        elif "tinyurl" in domain:
            pass
        else:
            domains.append(domain)

    return domains


with open("extracted_linkls.json") as ff:
    videos = json.load(ff)

videos_len = len(videos)
domains = []
for id, links in videos:
    print(f'executing video number {len(domains)+1} out of {videos_len}')
    domains.append(interpret_links(links))

with open('link_domains2.json','w') as ff:
    json.dump(domains, ff)
