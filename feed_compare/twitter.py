import json
import tweepy
import regex

from .tokens import ACCESS_TOKENS, CONSUMER_SECRET, CONSUMER_KEY

api_global = None

def get_api():
    global api_global
    if api_global:
        return api_global

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKENS[0][1], ACCESS_TOKENS[0][2])

    api_global = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api_global


def user_timeline(screen_name, count):
    api = get_api()
    try:
        statuses = api.user_timeline(screen_name=screen_name, count=count, trim_user=True, tweet_mode='extended')
    except:
        print('Error with {}, user likely deleted or suspended.'.format(kwargs))
        return False
    return statuses


def get_timeline_urls(screen_name, count):
    tweets = user_timeline(screen_name, count)
    urls = [t.entities.get('urls')[0].get('expanded_url') if len(t.entities.get('urls'))>0 else '' for t in tweets]
    urls = [x for x in urls if x] # Remove empty URL strings
    urls = [x for x in urls if regex.search('instagram', x) is None] #Remove URLs which are Instagram posts
    return urls


if __name__ == '__main__':
    print(get_timeline_urls('CNN', 5))
