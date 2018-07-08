# !pip3 install news-please
# !pip3 install fuzzywuzzy
# !pip3 install python-Levenshtein

# key info
from keysecret import keys
key_info = keys['info']

# imports
from newsplease import NewsPlease
import string
import re
import requests
import json
import pandas as pd
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class InputModel:
    """ Yields information about the input url """

    def __init__(self, url):
        self.article = NewsPlease.from_url(url)

    def title(self):
        return self.article.title

    def image(self):
        return self.article.image_url

    def source(self):
        return self.article.source_domain

class GetBias(InputModel):
    """ Yields bias classification for major news link """
    def __init__(self, url):
            InputModel.__init__(self, url)
    # returns image of news source bias
    def image(self):
        # define img url
        img_url = ''

        # load source bias data from all sides
        with open('allsides-media-bias-ratings.csv', mode='r') as infile:
            reader = csv.reader(infile)
            bias_dict = dict((rows[0],rows[1]) for rows in reader)

            # load source information from url
            the_source = self.source()
            new_source = the_source.split('.')[1]

            # create boilerplate stop list
            #remove_list = ['http://', 'https://', 'www', 'www1', 'com', 'org', 'net', 'int', 'edu' 'gov', 'mil', 'beta', 'eu', 'co', 'uk', 'europe', 'gma', 'blogs', 'in', 'm', 'eclipse2017', 'money']

            #for seq in remove_list:
                    #if seq in the_source:
                        #new_source=the_source.replace(seq,"")

            # using fuzzy match, find the All Sides source that best matches the input url
            mapping = []
            for listed_source in bias_dict:
                match = fuzz.token_set_ratio(listed_source, new_source)

                if match > 65:
                    if len(mapping) == 0:
                        mapping = [match, listed_source, bias_dict[listed_source]]
                    elif match > mapping[0]:
                        mapping = [match, listed_source, bias_dict[listed_source]]

            # if a match was found, select image corresponding to source bias
            if len(mapping) != 0:
                Left = ['Lean Left', 'Left']
                Right = ['Lean Right', 'Right']
                Center = ['Center']

                if mapping[2] in Left:
                    img_url='https://raw.githubusercontent.com/pkipsy/news-lens/master/Flask-App/graphics/left.jpg?raw=true'
                elif mapping[2] in Right:
                    img_url='https://raw.githubusercontent.com/pkipsy/news-lens/master/Flask-App/graphics/right.jpg?raw=true'
                elif mapping[2] in Center:
                    img_url='https://raw.githubusercontent.com/pkipsy/news-lens/master/Flask-App/graphics/center.jpg?raw=true'

            #info = {the_source: mapping}
            else:
                img_url='https://raw.githubusercontent.com/pkipsy/news-lens/master/Flask-App/graphics/uncertain.jpg?raw=true'
                #info = {the_source: 'Uncertain'}

        return mapping[2]

class OutputModel:
    """ Yields scraped data about the input url """

    def __init__(self, url):
        self.article = NewsPlease.from_url(url)

    # given URL, extract & clean article information from NewsPlease
    def process(self):
        # reduce article size
        input_text = self.article.title+" "+self.article.text[0:200]

        # clean article text
        input_text = input_text.replace('\n',' ')
        banned = ["’","’","“","—","”","‘","–"]
        banned = ''.join(banned) + string.punctuation
        translation_table = dict.fromkeys(map(ord, banned), ' ')
        unicode_line = input_text.translate(translation_table)
        unicode_line = re.sub(' +',' ',unicode_line)

        return(unicode_line)

class News(InputModel, OutputModel):

    def __init__(self, url):
        InputModel.__init__(self, url)
        OutputModel.__init__(self, url)

    # gather similar articles from Lateral
    def lateral_query(self):
        url = "https://news-api.lateral.io/documents/similar-to-text"
        payload = "{\"text\":\""+self.process()+"\"}"
        headers = {
          'subscription-key': key_info,
          'content-type': "application/json"
          }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    # write news information to a dataframe
    def store_news(self):
        sim_dict = {'sim':[], 'source':[], 'date':[], 'title':[], 'url':[], 'image':[], 'summary':[]}
        query = self.lateral_query()
        json_data = json.loads(query)
        for i in range(0,len(json_data)):
            sim_dict['title'].append(json_data[i]['title'])
            sim_dict['url'].append(json_data[i]['url'])
            sim_dict['date'].append(json_data[i]['published'][0:10])
            sim_dict['image'].append(json_data[i]['image'])
            sim_dict['summary'].append(json_data[i]['summary'])
            sim_dict['source'].append(json_data[i]['source_name'])
            sim_dict['sim'].append(json_data[i]['similarity'])

        sim_articles = pd.DataFrame(sim_dict, columns=['sim', 'source', 'date', 'title', 'url', 'image', 'summary'])
        return sim_articles

    # assess news source bias with all sides ratings
    def match_bias(self):
        # load source bias data from all sides
        with open('allsides-media-bias-ratings.csv', mode='r') as infile:
            reader = csv.reader(infile)
            bias_dict = dict((rows[0],rows[1]) for rows in reader)

            # calculate the match between source names, add highest matches to mapping dict
            sim_articles = self.store_news()
            mapping = {}

            for new_source in sim_articles['source']:
                for listed_source in bias_dict:
                    match = fuzz.token_set_ratio(listed_source, new_source)

                    '''
                    if there is a strong match, create a link in the dictionary
                    if the dictionary already has an entry, only replace it if this match is stronger
                    if the match < 64, list the source bias as "uncertain"
                    '''

                    if match > 65:
                        if new_source not in mapping:
                            mapping[new_source] = [match, listed_source, bias_dict[listed_source]]
                        elif match > mapping[new_source][0]:
                            mapping[new_source] = [match, listed_source, bias_dict[listed_source]]
                    else:
                        if new_source not in mapping:
                            mapping[new_source] = [match, listed_source, 'Uncertain']
                        elif match > mapping[new_source][0]:
                            mapping[new_source] = [match, listed_source, 'Uncertain']

        return mapping

    def add_bias(self):
        placeholder = []
        sim_articles = self.store_news()

        for row in sim_articles['source']:
            if row in self.match_bias():
                placeholder.append(self.match_bias()[row][2])
            else:
                placeholder.append('None')

        sim_articles['bias'] = placeholder

        return sim_articles

    # select news for website
    def choose_news(self):
        updated_articles = self.add_bias()
        select_news = {'source':[], 'title':[], 'url':[],'image':[], 'bias':[]}

        for i in range(0,updated_articles.shape[0]):

            # make sure the "similar" retrieved documents are not identical to the input
            similar_title = updated_articles.loc[i]['title']
            if similar_title != self.title():

                source = updated_articles.loc[i]['source']
                if source not in select_news['source']:

                    select_news['source'].append(source)
                    select_news['title'].append(similar_title)
                    select_news['url'].append(updated_articles.loc[i]['url'])
                    select_news['image'].append(updated_articles.loc[i]['image'])
                    select_news['bias'].append(updated_articles.loc[i]['bias'])

        return select_news

class Wiki(OutputModel):

    def __init__(self, url):
        OutputModel.__init__(self, url)

    # gather wikipedia articles from Lateral
    def lateral_query(self):
        url = "https://wikipedia-api.lateral.io/recommend-by-text/"
        payload = "{\"text\":\""+self.process()+"\"}"
        headers = {
          'subscription-key': key_info,
          'content-type': "application/json"
          }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    # write wiki information to a dataframe
    def store_wiki(self):
        response_wiki = self.lateral_query()

        sim_dict_wiki = {'sim':[], 'title':[], 'url':[]}
        json_data = json.loads(response_wiki)

        for i in range(0,len(json_data)):
            sim_dict_wiki['title'].append(json_data[i]['title'])
            sim_dict_wiki['url'].append(json_data[i]['url'])
            sim_dict_wiki['sim'].append(json_data[i]['similarity'])

        sim_wiki = pd.DataFrame(sim_dict_wiki, columns=['sim', 'title', 'url'])
        return sim_wiki

    # select wiki pages for website
    def choose_wiki(self):
        sim_wiki = self.store_wiki()
        select_wiki = {'title':[], 'url':[]}

        for i in range(0,sim_wiki.shape[0]):

            select_wiki['title'].append(sim_wiki.loc[i]['title'])
            select_wiki['url'].append(sim_wiki.loc[i]['url'])

        return select_wiki
