# Visualization Notebooks

### [LDA-Viz](https://github.com/pkipsy/news-lens/blob/master/Visualization/LDA-Viz.ipynb)
This notebook relies on the open source Python library, [PyLDAviz](https://github.com/bmabey/pyLDAvis), for interactive topic model visualization. 
Separate models and visualizations have been created for left, right, and center-leaning media articles, from the All Sides headline crawl.
Each visualization makes it possible to explore the latent topics in these texts, along with the words that are most closely associated with them. 
There is a lot to uncover! The Russia investigation, school shootings, terrorism, and climate change, are just a few of the topics that vary in their coverage across party lines.

### [Scattertext](https://github.com/pkipsy/news-lens/blob/master/Visualization/Scattertext.ipynb)*
This notebook uses the open source Python library, [Scattertext](https://github.com/JasonKessler/scattertext), to illustrate differences between left and right-leaning media. 
It identifies key topics that are characteristic of both sides, as well as topics that are used more frequently by one side or the other. 
These differences are visible for both very common words (like <i>Donald Trump</i>) and rarer words (like <i>CBO</i>). 

### [Sentiment+Analysis](https://github.com/pkipsy/news-lens/blob/master/Visualization/Sentiment%2BAnalysis.ipynb)
Examines the distribution of sentiment across news articles, an analysis made possible by Google's [Natural Language API](https://cloud.google.com/natural-language/). 

* Computationally intensive. Run on Google Cloud's [Data Lab](https://cloud.google.com/datalab/) or Amazon's [Sagemaker](https://aws.amazon.com/sagemaker/).
