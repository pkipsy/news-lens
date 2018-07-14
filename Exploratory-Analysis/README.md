# Exploratory Notebooks

### Media Bias: [Score Comparison](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/05%20-%20FilterBubbles-MediaBias.ipynb)
Compares All Sides Media's [bias scores](https://www.allsides.com/media-bias/media-bias-ratings) to the numerical ratings reported in the [academic article](http://sethrf.com/files/bubbles.pdf), "Filter Bubbles, Echo Chambers, and Online News Consumption".

### Google Cloud: [Sentiment Analysis](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Sentiment-Analysis.ipynb)
Examines the distribution of sentiment across news articles with Google's [Natural Language API](https://cloud.google.com/natural-language/). Compares sentiment across bias classes.

### Google Cloud: [Named Entity Recognition](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Entities-Analysis.ipynb)
Performs named-entity recognition with Google's [Natural Language API](https://cloud.google.com/natural-language/), where entities are common noun clusters, such as people, organizations, and events.
Extracts and classifies entities in text collections and records their relative salience.
Plots differences between conservative and liberal entities.

### Gensim: [Topic Modeling](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Topic-Modeling.ipynb)
A simple exercise implementing topic models with [gensim](https://radimrehurek.com/gensim/) over political news articles.

### fastText: [Text Classification](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/TextClassification-fastText.ipynb)
Runs Facebook's [fastText](https://github.com/facebookresearch/fastText/tree/master/python), an unsupervised learning algorithm for efficiently computing word embeddings.

### scikit-learn: [Decision Tree](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Decision-Tree.ipynb)
Implements a simple decision tree on the All Sides Crawl with scikit-learn.
