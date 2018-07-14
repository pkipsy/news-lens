# News Scraping 

## Scrapers

### Beautiful Soup: [All Sides Headline Crawler](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/01%20-%20AllSidesMedia-HeadlineCrawler.ipynb)
This notebook showcases the Beautiful Soup spider used to crawl [All Sides Media](https://www.allsides.com/story/admin). This spider extracts information about the last two years of headline roundups. 
For every roundup, it harvests the All Sides' headline and short summary, as well as information about the linked articles (such as their source, their source's bias, their source's headline, and so on).
The initial crawl pulled ~3,500 news links.

### Webhose.io: [Recent News Crawl](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/06%20-%20Webhose-Scrape.ipynb)
A series of crawls configured to extract English language texts published in the US over the last thirty days from select media organizations, using [Webhose.io](https://webhose.io/web-content-api).
The initial run pulled 30,000+ news articles.

### Google Results Scraper: [Source ID](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/04%20-%20Source-Classification.ipynb)
[Google Results Scraper](https://github.com/NikolaiT/GoogleScraper) is deployed to identify the website url for all the news sources rated by All Sides Media.

## Extractors

### NewsPlease: [Article Extraction](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/02%20-%20NewsPlease-ArticleExtraction.ipynb)
This notebook uses the open source Python library, [NewsPlease](https://github.com/fhamborg/news-please), to extract information from articles harvested by the Beautiful Soup crawler.

### BoilerPipe: [Article Extraction](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/03%20-%20BoilerPipe-ArticleExtraction.ipynb)
[Boilerpipe](http://boilerpipe-web.appspot.com/) offers an alternative method for article extraction.

# Future Projects
Having tested many combinations of news crawlers and extractors, my top recommendation for all-around functionality is [NewsPaper3k](https://github.com/codelucas/newspaper) (July 2018).
