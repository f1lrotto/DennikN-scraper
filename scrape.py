import requests
import json
from bs4 import BeautifulSoup

URL = 'https://dennikn.sk/minuta/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

posts = soup.find_all("div", class_="mnt-Post-hash")

post_dict = {}

for post in posts:
    post_child = post.find(
        "div", class_='mnt-FeedArticle js-hook-feed-article')
    post_grandchild = post_child.find("div", class_='mnt-toolbar')
    
    link_to_post = post_grandchild.find(href=True)
    link_to_post = link_to_post['href']
    
    post_id = post.get('id')
    dict_entry_name = 'post-'+post_id
    
    post_dict[dict_entry_name] = {'postID': post_id, 'postLink': link_to_post}
    

json_posts = json.dumps(post_dict)

print(json_posts)