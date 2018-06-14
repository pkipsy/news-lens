'''
BoilerPipe for Article Extraction

BoilerPipe is a project of Kohlschütter Search Intelligence. BoilerPipe "provides
algorithms to detect and remove the surplus "clutter" (boilerplate, templates) around
the main textual content of a web page." In short, it's great for parsing news articles.

While there are python wrappers for BoilerPipe, here we are making use of its Web API,
which returns better-cleaned .json.
'''

# import modules
import urllib.request
import urllib.error
import time
from bs4 import BeautifulSoup

'''
Here we load links harvested with our All Sides Media spider.
'''

# load news links harvested from spider
with open('link_file.txt') as f:
    news_links = [line for line in f]

'''
To successfully query BoilerPipe's Web API, we need to make some minor changes to
the link format.
'''

updated_links = []

# reformat links to successfully query BoilerPipe's web API
def reformat_links(news_links):
    for link in news_links:
        new_link = link.replace(':', '%3A')
        new_link = new_link.replace('/','%2F')

        link_start = 'https://boilerpipe-web.appspot.com/extract?url='
        link_end = '&extractor=ArticleExtractor&output=json&extractImages=&token='
        new_link = link_start + new_link + link_end

        clean_link = new_link.replace("\n", "")

        updated_links.append(clean_link)

reformat_links(news_links)

'''
We can now set about iterating through our list of links, and parsing the news articles
through BoilerPipw's Web API. The article content will be returned to us in .json.
'''

# query BoilerPipe's web API, retrieving and storing json summaries
article_collection = []
def scrape_page(updated_links):
    for url_query in updated_links:
        try:
            page = urllib.request.urlopen(url_query)
            time.sleep(5)
            article_collection.append(page)
        except HTTPError:
            article_collection.append('Pay Wall')

scrape_page(updated_links)

# read information to json
import json
with open('newsarticle-texts.txt', 'w') as outfile:
    json.dump(article_collection, outfile, ensure_ascii=False)
