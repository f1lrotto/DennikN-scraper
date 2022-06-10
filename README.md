# DennikN-scraper
## Introduction
This is a microservice created to be used alongside with [discord news alert](https://github.com/f1lrotto/news-from-dennik-n-discord-alert) service, to get the latest news from the news website DennikN. 

## Functionality
The server is listening on [http://localhost:3000/posts](http://localhost:3000/posts) for incoming `GET` requests.

After a request is made, it proceedes to screape DennikNs [Minuta po minute](https://dennikn.sk/minuta) website. 

When it's done scraping, it returns a JSON with the latest 35 articles, each containing a:
- `postID` - ID of a news article that is assigned by DennikN
- `postTime` - Time when was the article published
- `postLink` - Link to the article itself
- `headline` - Headline for the article

## Running the project

### Installing the dependancies
These are the dependancies used for this application, if you have any of them on your system already installed, you may skip that particular one.

**Flask**
```
pip install flask
```
**BeautifulSoup**
```
pip install BeautifulSoup
```
**datetime**
```
pip install datetime
```
### Running the application
```
python3 app.py
```
