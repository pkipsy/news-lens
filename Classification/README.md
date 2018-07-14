# All Sides Media Crawl

### [Preprocessing](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Preprocessing.ipynb)
Performs text cleaning on the All Sides crawl. Adds additional features, including: sentiment (valence and magnitude), text readability, text length, and publication date. Saves cleaned file to csv.

### [Classification](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Models.ipynb)
Defines and explores text features and how they vary across bias groups. Creates a classifier pipeline incorporating multiple features. Implements stratified k-folds cross validation and parameter grid search. Generates a classification report. Plots a confusion matrix. Plots learning curve over training. Includes comparison between Multinomial Bayes and SVC.

### [Model Comparison](https://github.com/pkipsy/news-lens/blob/master/Classification/Model-Comparison.ipynb)* 
Compares classification performance of a variety of learning algorithms (e.g., SVC, Bernoulli, Multinomial Naive Bayes, and word embeddings) and text transformations (bag of words vs TF-IDF).

# Webhose.io Crawl

### [Preprocessing](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Preprocessing-Webhose.ipynb)
Performs text cleaning on the webhose.io crawl. Adds a text readability measure. Creates a separate cleaned version for the [ShortText algorithm](https://shorttext.readthedocs.io/en/latest/index.html). 

### [Classification](https://github.com/pkipsy/news-lens/blob/master/Classification/Classification-Models-Webhose.ipynb)
Defines and explores text features and how they vary across bias groups. Creates a classifier pipeline incorporating multiple features. Runs a Linear SVC, with and without the news source feature. Examines accuracy on train and test sets, as well as generalization to the All Sides crawl.

* All notebooks are computationally intensive. Run on Google Cloud's [Data Lab](https://cloud.google.com/datalab/) or Amazon's [Sagemaker](https://aws.amazon.com/sagemaker/).
