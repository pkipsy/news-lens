# !pip install news-please
# !pip install fuzzywuzzy
# !pip install python-Levenshtein
# !pip install scattertext
# !pip install spacy
# !python -m spacy download en
# !pip install future

# imports url transformer to analyze input url and get a recommended article
from sandbox import InputModel, OutputModel, News

# import scattertext modules
import scattertext as st
import re, io
from pprint import pprint
import pandas as pd
import numpy as np
from scipy.stats import rankdata, hmean, norm
import spacy
import os, pkgutil, json, urllib
from urllib.request import urlopen
from scattertext import CorpusFromPandas, produce_scattertext_explorer
nlp = spacy.load('en')

# import text processing modules
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

class Viz(News):

    def __init__(self, url):
        News.__init__(self, url)

    def get_texts(self):
      '''
      get text of input url & first recommended article
      write to dataframe with bias information
      '''

      # load text of user input
      user_input = self.article.text
      user_input = user_input.split('\n')

      # load text of top recommended article
      rec_article = self.choose_news()
      rec_url = rec_article['url'][0]
      rec_text = OutputModel(rec_url).article.text
      rec_text = rec_text.split('\n')

      # create dataframe
      text = user_input + rec_text
      bias = ['right']*len(user_input)+['left']*len(rec_text)
      position = list(range(0,len(text)))
      data = {'bias':bias, 'position':position, 'text':text}
      df = pd.DataFrame(data, columns = ['bias', 'position', 'text'])

      # shuffle df for random sampling
      df = df.sample(frac=1).reset_index(drop=True)

      return df

    def clean_texts(self):
      ''' text preprocessing '''

      df = self.get_texts()

      # rewrite df with cleaned text
      for i in range(0, len(df)):
        text = df.at[i,'text']

        text = text.lower()
        text = text.replace('\n',' ')

        numbers = ['0','1','2','3','4','5','6','7','8','9']
        banned = ["’","’","“","—","”","‘","–",'#','[','/','(',')','{','}','\\','[',']','|','@',',',';','+','-']
        banned = ''.join(banned) + ''.join(numbers)
        banned = banned.replace(".", "")
        stop_list = set(stopwords.words('english'))

        translation_table = dict.fromkeys(map(ord, banned), ' ')
        text = text.translate(translation_table)
        text = re.sub(' +',' ',text)
        text = ' '.join([word for word in text.split() if word not in stop_list])

        df.at[i,'text'] = text

      return df

    def create_corpus(self):

      # load cleaned df
      convention_df = self.clean_texts()

      # create parsed corpus
      convention_df.groupby('bias').apply(lambda x: x.text.apply(lambda x: len(x.split())).sum())
      convention_df['parsed'] = convention_df.text.apply(nlp)
      corpus = st.CorpusFromParsedDocuments(convention_df, category_col='bias', parsed_col='parsed').build()

      # remove stop words
      stop_word_list = ['via getty', 'inbox', 'subscribe', '×', 'close ×', 'screen close', 'full screen', 'buy second', 'second continue', 'story continued', 'llc permission', '―', 'xe', '\\xe2\\x80\\x99', 'news', 'for reprint', 'llc', 'post', 'click', 'to', '’ve', 'unsupported on', 'share', 'that ’s', 'still', 'got', 'it', '37', 'of his', 'this report', 'ofs', 'fox', 'photos', '’m', 'is the', 's.', 'around', 'times', 'also', 'the', 'copyright', 'washington times', 'mr', 'press', 'wait', 'associated', 'unsubscribe', 'view', 'photo wait', 'http', '#', 'associated press', 'more videos', 'get', 'just watched', 'permission', 'however', 'b.', 'ms.', 'here©', 'device', 'copyright ©', 'paste', '10', 'the associated', 'contributed to', 'hide', 'and his', 'videos', 'said mr.', '_', '©', 'contributed', 'embed', 'n’t', '/', 'something', 'i', 'that they', 'read', 'for a', 'playback', 'must watch', 'washington post', 'just', 'to get', 'r', 'read more', 'toggle', 'more', 'i ’m', 'follow', 'is', 'https', ' ', 'said', 'mr.', 'unsupported', 'or blog', 'your device', 'for', 'cnn', 'of 76', 'that', 'ms', 'andhis', 'click here', 'or share', 'replay', 'press contributed', 'they', 'must', 'prof', 'www', 'it ’s', 'told', '’re', 'the washington', '1', "'s rise", '© 2018', 'to this', 'skip', 'around the', 'blog', 'cut', 'told fox', 'mrs.', 'hide caption', 'ad', 'watched', '/ the', 'replay more', 'and the', '’s', '2018', 'copy', '&', 'read or', 'reprint permission', 'are', 'told cnn', 'watch', 'here for', 'also said', 'copy this', 'reprint', 'report', 'advertisement', 'mrs', 'caption', 'autoplay', 'fox news', 'dr', 'enlarge', 'times llc', '76', 'photo', 'this']
      stop_word_list = list(set(stop_word_list))

      update_stop = []
      for term in stop_word_list:
        if term in corpus._term_idx_store:
          update_stop.append(term)
      corpus = corpus.remove_terms(update_stop)

      return corpus

    def scatter_viz(self):

      #load corpus
      corpus = self.create_corpus()

      #load cleaned df
      convention_df = self.clean_texts()

      html = produce_scattertext_explorer(corpus,
                                    category='left',
                                    category_name='Democratic',
                                    not_category_name='Republican',
                                    width_in_pixels=1000,
                                    minimum_term_frequency=1,
                                    metadata=convention_df['position'],
                                    term_significance = st.LogOddsRatioUninformativeDirichletPrior())

      file_name = 'templates/scattertext.html'
      open(file_name, 'wb').write(html.encode('utf-8'))

      return html
