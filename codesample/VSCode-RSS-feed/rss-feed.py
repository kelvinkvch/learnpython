import datetime
import logging

import azure.functions as func
import requests
from bs4 import BeautifulSoup


def main(mytimer: func.TimerRequest) -> None:
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    url = "https://code.visualstudio.com/feed.xml"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    article_list = []
    articles = soup.findAll('entry', limit=3)

    for a in articles:
        article_title = a.title.text
        article_link = a.id.text
        article_date = a.updated.text[:10]

        print ("Title: {}".format(article_title))
        print ("Updated: {}".format(article_link))
        print ("Published: {} \n".format(article_date))
