import json
import yaml
from watson_developer_cloud import PersonalityInsightsV3
import twitterscraper
from datetime import datetime
from dateutil import parser



def fetch_tweets(username):
    tweets = twitterscraper.tweets(username)
    content_items = {}
    content_items['contentItems'] = []

    for tweet in tweets:
        item = {
            'id': 'TW'+str(tweet.id),
            'content': tweet.text,
            'contenttype': 'text/plain',
            'created': parser.parse(tweet.created_at).timestamp(),
            'forward': tweet.retweeted, 
            'reply': bool(tweet.in_reply_to_screen_name),
        }
        content_items['contentItems'].append(item)

    return content_items


def personality_insights(data):
    with open('creds.yaml') as file:
        creds = yaml.load(file)

    insights = PersonalityInsightsV3(
        version='2016-10-20',
        username=creds['IBM']['ServiceUsername'],
        password=creds['IBM']['ServicePassword'])

    profile = insights.profile(data, content_type='application/json',
                                           raw_scores=False, consumption_preferences=True)
    return json.dumps(profile, indent=2)


# personality_insights(fetch_tweets('SkullTech101'))
