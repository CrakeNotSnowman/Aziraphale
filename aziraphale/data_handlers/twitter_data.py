

import kmlistfi
import tweepy
import json

from utils import locateDB


'''
This module will suffer from two independent goals, 
goal A (the dominating goal): be able to interact with twitter
    data easily from any program
goal B (the original goal): Replace tweepy in tests

While building out goal B, it quickly became apparent that simply 
    interacting with the twitter data I have saved is a large enough
    task, and that it will be a similar task with wikipedia data, 
    reddit data, stack overflow data, and so on. Therefore it makes 
    sense to group a lot of the 'interact with datasets/databases' 
    functions in a library, and draw from that library in goal B 

Sample Tweets 1:
June 14th 2019-July 8th 2019
Various Uptime, primary computer
Sample Tweets 2:
July 8th 2019-August 3rd 2019
fairly constant, (gap at 3 am to ~5 am), raspberry pi



consider building a class `tweet_itterator` which loads all possible 
tweet paths, and then runs through and itterates over them for the user

with attributes for 
    get_random_tweet
    get_random_sample
    get_

Also, Event Specific Attributes, 
    same idea, but a collection of only 'thunder' tweet sample paths


'''
class Twitter_DS_Interactions(object):
    def __init__(self, paths):
        self.source_paths = paths['sample1'] + paths['sample2']



def sample_tweets1_path_full():
    possible_locations = ["/media/keith/hdd01/Databases/Twitter/sample_tweets1/"]
    return possible_locations
def sample_tweets2_path_full():
    possible_locations = ["/media/keith/hdd01/Databases/Twitter/sample_tweets2/"]
    return possible_locations

def get_file_paths_full():
    check_here = {}
    check_here['samples1'] = sample_tweets1_path_full()
    check_here['samples2'] = sample_tweets2_path_full()
    paths = locateDB.get_db_file_locations(check_here)
    return paths
    


class fake_api(object):
    '''
    Object Goal: pretend to be a tweepy api object

    Function Calls it must replicate:
    api.me().screen_name.encode('utf-8')

    api.search
    tweetList = tweepy.Cursor(api.search,
                q=event,
                rpp=rppSize,
                result_type="recent",
                include_entities=True, 
                tweet_mode='extended').items()

    api.update_with_media(fn, status=msg)

    '''

    def __init__(self):
        pass


def load_recent_tweets_from_file(filePath):
    with open(filePath) as ifl:
        all_tweets = json.load(ifl)
    n = len(all_tweets)
    i = 0
    perc = 0
    for tweets_json_list in all_tweets:
        if int(i/n*10) > perc: # Show in 10% chunks
            print('\tLoading... ' + str(100*i/n) + '%')
            perc = int(i/n)*10
        tweets = [tweepy.models.Status().parse(None, tweet) for tweet in tweets_json_list]

    return tweets

def get_new_tweets():


    return


def get_event(event_Name, m_samples_before, 
                n_samples_after):


    return 

def make_annotation(file_path, annotation:str):

    return


def load_tweets(**kwargs):
    eventName = None
    start_date = None
    end_date = None
    duration = None
    sample_count = None
    tweet_count = None 
    return

def load_n_tweets(n):

    # Hard coded specific blocks
    samp1basepath = locateDB['samp1']
    samp2basepath = locateDB['samp2']