# A simple job aggregator from  Hacker News with the use of it's API
# Karima H - June 2023

import requests
import time
import pyfiglet as pf

#make a call to the API
print('\033[1;33;40m')
print('\033[1;33;40m',pf.figlet_format('Hacker News Jobs'),'\033[1;37;40m')
url = 'https://hacker-news.firebaseio.com/v0/jobstories.json'
result = requests.get(url)

offer_ids = result.json()
offers = []
print("...Gathering your job offers...")

#process each jobs with their info
for offer_id in offer_ids[:10]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{offer_id}.json"
    result = requests.get(url)
    data_collected = result.json()
    offer = {
        'title': data_collected['title'],
        'author': data_collected['by'],
        'hn_link': f"http://news.ycombinator.com/item?id={offer_id}",
    }
    offers.append(offer)

#print out all the info collected from each job offer
for offer in offers:
    print(f"\033[1;34;40m\nOffer: {offer['title']}\033[1;37;40m")
    print(f"Author: {offer['author']}")
    print(f"URL: {offer['hn_link']}")
    time.sleep(0.2)