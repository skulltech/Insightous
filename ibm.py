import json
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

    print(content_items)


def personality_insights(username, password, data):
    insights = PersonalityInsightsV3(
        version='2016-10-20',
        username='YOUR SERVICE USERNAME',
        password='YOUR SERVICE PASSWORD')

    profile = personality_insights.profile(data, content_type='application/json',
                                           raw_scores=True, consumption_preferences=True)
    print(json.dumps(profile, indent=2))


fetch_tweets('SkullTech101')
