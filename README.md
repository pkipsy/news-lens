# news-lens
## Filtering out Political Bias in American News Media

<p align="center"><img src="http://assets.pewresearch.org/wp-content/uploads/sites/12/2016/04/PP_16.04.26_polarization.gif"></p>

Today is a time of increasing political and cultural polarization in the United States. Our media reflects this polarization, with right and left-leaning outlets providing substantively different takes on the same breaking news.

The bipartisan organization [All Sides](http://allsides.com/) looks to provide a more balanced approach to news coverage by rounding up the top headlines of the day and showcasing reporting of these stories by outlets on the left, right, and center. This expert curation is invaluable to the continued health of our democracy.

The app [NewsLens](http://news-lens.online/) takes that kernel of insight and scales it, so that *any* news story or blog post can be approached from all sides. Input a link to a breaking story, and NewsLens will recommend related articles that offer divergent perspectives and identify points of common ground in reporting across the political divide.

## The Web App
With News Lens, you can input a news story you've been reading to quickly get some perspective on how its being reported. 
<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens.png?raw=true" width=75%></p>

First, NewsLens identifies the article, and gives an estimated bias score. 
<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens_classify.png?raw=true" width=75%></p>

Next, the app recommends recent articles that are on the same topic, but from sources on the other side of the aisle, as well as reference articles on the issues from Wikipedia.
<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-related.png?raw=true" width=75%></p>

Finally, the app renders an interactive visualization of the conversation, showing similarities and differences in how liberal and conservative sources are talking about the same story.
<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-visualize.png?raw=true" width=75%></p>

## How It Works
Interested in learning more about this how this app works? Check out the jupyter notebooks in the project folders.

### News Scraping
The [News Scraping](https://github.com/pkipsy/news-lens/tree/master/News-Scraping) notebooks delve into the choice of data source, as well as methods of data collection and extraction. <br/>
**Tools**: Beautiful Soup, NewsPlease, Newspaper3k, BoilerPipe, Google Results Scraper.

### Exploratory Analysis
The [Exploratory](https://github.com/pkipsy/news-lens/tree/master/Exploratory-Analysis) notebooks cover a range of early-stage investigations of the scraped texts, including sentiment analysis, named entity recognition, topic modeling, and word embeddings. <br/>
**Tools**: Google Natural Language API, Gensim, fastText, Sklearn.

### Visualization
The [Viz](https://github.com/pkipsy/news-lens/tree/master/Visualization) notebooks explore a variety of interactive visualization techniques for text data. <br/>
**Tools**: ScatterText, PyLDAViz.

### Classification
The [Classification](https://github.com/pkipsy/news-lens/tree/master/Classification) notebooks run through data preprocessing, feature engineering, feature pipelines, parameter tuning, model performance, and model comparison. <br/>
**Tools**: Sklearn, NumPy, SciPy, Matplotlib, Seaborn, gLoVe, word2vec, shortText.

### Web App
The [Web App](https://github.com/pkipsy/newslens-app) repo contains the Flask app deployed on Amazon Web Services. <br/> **Tools**: Flask, Bootstrap, HTML, CSS, js.
