# DennikN-scraper
## Introduction
This is a microservice created to be used alongside with [Discord-News](https://github.com/f1lrotto/news-from-dennik-n-discord-alert), to get the latest news from the news website DennikN, served to a discord server chat. 

## Functionality
The server is listening on [https://dennik-n-scraper.herokuapp.com/posts](https://dennik-n-scraper.herokuapp.com/posts) for incoming `GET` requests.

After a request is made, it proceedes to screape DennikNs [Minuta po minute](https://dennikn.sk/minuta) website. 

When it's done scraping, it returns a JSON with the latest 35 articles, each containing a:
- `postID` - ID of a news article that is assigned by DennikN
- `postTime` - Time when was the article published
- `postLink` - Link to the article itself
- `headline` - Headline for the article

## Running the project

### Installing the dependencies
These are the dependencies used for this application, if you have any of them on your system already installed, you may skip that particular one.

```
pip install flask beautifulsoup4 datetime requests waitress
```

### Running the application
```
python3 app.py
```
