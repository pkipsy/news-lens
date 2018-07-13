# Exploratory Notebooks

### Media Bias: [Score Comparison](https://github.com/pkipsy/news-lens/blob/master/News-Scraping/05%20-%20FilterBubbles-MediaBias.ipynb)
Compares All Sides' bias scores to the numerical ratings reported in [Filter Bubbles, Echo Chambers, and Online News Consumption](http://sethrf.com/files/bubbles.pdf).

### Google Cloud: [Named Entity Recognition](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Entities-Analysis.ipynb)
Performs named-entity recognition with Google's [Natural Language REST API](https://cloud.google.com/natural-language/). 
Extracts and classifies entities (such as people, organization, and events) in text collections and records their relative salience.
Plots differences between conservative and liberal entities.

### Gensim: [Topic Modeling](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Topic-Modeling.ipynb)
A simple exercise implementing topic models with gensim over political news articles.

### fastText: [Text Classification](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/TextClassification-fastText.ipynb)
Runs Facebook's [fastText](https://github.com/facebookresearch/fastText/tree/master/python), an unsupervised learning algorithm for efficiently computing word embeddings.

### [Model Comparison](https://github.com/pkipsy/news-lens/blob/master/Exploratory-Analysis/Model-Comparison.ipynb)
Compares classification performance of a variety of learning algorithms (e.g., SVC, Bernoulli, Multinomial Naive Bayes, and word embeddings) and text transformations (bag of words vs TF-IDF).
Computationally intensive - run on Google Cloud's [Data Lab](https://cloud.google.com/datalab/).
