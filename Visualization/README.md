# Visualization Notebooks

### [LDA-Viz](https://github.com/pkipsy/news-lens/blob/master/Visualization/LDA-Viz.ipynb)
This notebook creates interactive topic model visualizations with the open-source Python library [PyLDAviz](https://github.com/bmabey/pyLDAvis). 
Separate models and visualizations are constructed for left, right, and center-leaning news articles, from the [All Sides Media](https://www.allsides.com/unbiased-balanced-news) headline crawl.
Each visualization makes it possible to explore the latent topics in these text collections, along with the words that are most closely associated with them. 
There is a lot to uncover! The Russia investigation, school shootings, terrorism, and climate change, are just a few of the topics that vary in their coverage across party lines.

### [Scattertext](https://github.com/pkipsy/news-lens/blob/master/Visualization/Scattertext.ipynb)*
This notebook illustrates differences between left and right-leaning media with the open-source Python library [Scattertext](https://github.com/JasonKessler/scattertext). 
The visualization showcases key topics that are of interest to both sides, as well as topics that are used more frequently by one side or the other. 
These differences are visible both for very common words (like <i>Donald Trump</i>) and rarer words (like <i>CBO</i>). 

### [Sentiment Analysis](https://github.com/pkipsy/news-lens/blob/master/Visualization/Sentiment%2BAnalysis.ipynb)
This notebook examines the distribution of sentiment across news articles, an analysis made possible by Google's [Natural Language API](https://cloud.google.com/natural-language/). 

* Computationally intensive. Run on Google Cloud's [Data Lab](https://cloud.google.com/datalab/) or Amazon's [Sagemaker](https://aws.amazon.com/sagemaker/).
