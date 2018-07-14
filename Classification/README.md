# All Sides Media Crawl

### [Preprocessing](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Preprocessing.ipynb)

Preprocesses text from the All Sides crawl with [nltk](https://www.nltk.org/) and [pandas](https://pandas.pydata.org/). 

<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-preprocessing.png?raw=true" width=75%></p>

Performs feature engineering. Added features include sentiment (valence and magnitude), text readability, text length, and publication date. Saves cleaned file to CSV.

<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-features.png?raw=true" width=75%></p>

### [Classification](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Models.ipynb)

Defines and explores text features and how they vary across bias groups, using [numpy](http://www.numpy.org/), [matplotlib](
https://matplotlib.org/), and [seaborn](https://seaborn.pydata.org/). Creates a classifier pipeline with [sklearn](http://scikit-learn.org/stable/) incorporating multiple features. Implements stratified k-folds cross validation and parameter grid search. Generates a classification report, noting precision, recall, and f1 score. Plots a confusion matrix and a learning curve over training. Compares performance between Multinomial Naive Bayes and Linear SVC.

<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-clfresults.png?raw=true" width=75%></p>

### [Model Comparison](https://github.com/pkipsy/news-lens/blob/master/Classification/Model-Comparison.ipynb)

Compares the classification performance of a variety of learning algorithms (including SVC, Bernoulli, Multinomial Naive Bayes, and word embeddings) and text transformations (bag-of-words vs TF-IDF).

<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-modelcomparison.png?raw=true" width=75%></p>

# Webhose.io Crawl

<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens-crawls.png?raw=true" width=75%></p>

### [Preprocessing](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Preprocessing-Webhose.ipynb)
Cleans text from the webhose.io crawl. Performs feature engineering. Creates a separate cleaned version for the [ShortText algorithm](https://shorttext.readthedocs.io/en/latest/index.html) and saves to JSON. 

### [Classification](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Models-Webhose.ipynb)
Defines and explores text features and how they vary across bias groups. Creates a classifier pipeline incorporating multiple features. Runs a Linear SVC, with and without the news source feature. Examines classification performance on train and test sets, as well as generalization to the All Sides crawl.

# General Note

All notebooks are computationally intensive. These were run either on Google Cloud's [Data Lab](https://cloud.google.com/datalab/) or Amazon's [Sagemaker](https://aws.amazon.com/sagemaker/). Google's free [Colaboratory](https://colab.research.google.com/) is also a decent option.
