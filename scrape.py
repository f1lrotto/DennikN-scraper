import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil import parser

URL = 'https://dennikn.sk/minuta/dolezite'

def getDate(link_to_post, post_list):
    page = requests.get(link_to_post)
    soup = BeautifulSoup(page.content, "html.parser")
    time = soup.find('time', class_="e_terms_term e_terms_posted")

    if time is None:
        time_obj = parser.parse(post_list[-1]['postTime'])
        dateObj = time_obj - timedelta(minutes=1)
        dateStr = dateObj.strftime('%Y-%m-%dT%H:%M:%S%z')
        dateStr = dateStr[:-2] + ':' + dateStr[-2:]
        return dateStr
    return time['datetime']


def get_data():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    posts = soup.find_all("div", class_="mnt-Post-hash", limit=35)

    post_list = []
    post_times = []
    for post in posts:
        post_child = post.find(
            "div", class_='FeedArticle__StyledArticle-sc-1afrvgs-0 mnt-FeedArticle js-hook-feed-article')
        mnt_toolbar = post_child.find("div", class_='mnt-toolbar')

        link_to_post = mnt_toolbar.find(href=True)

        link_to_post = link_to_post['href']

        mnt_article = post_child.find("div", class_='mnt-article')

        if mnt_article.find('a') != None:
            title = mnt_article.find('a')
            title = title.text
        else:
            title = mnt_article.find('p')
            if title.find('strong') != None:
                title = title.find('strong')
                title = title.text
        post_time = getDate(link_to_post, post_list)
        post_id = post.get('id')

        post_list.append({
            'postID': post_id, 'postTime': post_time, 'postLink': link_to_post, 'headline': title
        })

    json_posts = json.dumps(post_list)
    return json_posts
