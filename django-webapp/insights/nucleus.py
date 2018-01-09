import json
import yaml
from watson_developer_cloud import PersonalityInsightsV3
from dateutil import parser
import requests
import base64
from urllib.parse import quote_plus



def credentials(key, secret):
    creds = quote_plus(key) + ':' + quote_plus(secret)
    return base64.b64encode(creds.encode()).decode()


def bearer_token():
    with open('creds.yaml') as file:
        creds = yaml.load(file)

    headers = {
        'Authorization': 'Basic {}'.format(credentials(creds['Twitter']['ConsumerKey'], creds['Twitter']['ConsumerSecret'])),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'User-Agent': 'CodeFunDo-VAS App'
    }
    response = requests.post('https://api.twitter.com/oauth2/token', headers=headers, data={'grant_type': 'client_credentials'})
    return response.json()['access_token']


def timeline(username):
    token = bearer_token()
    payload = {
        'screen_name': username,
        'include_rts': True,
    }
    response = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json', 
                            headers={'Authorization': 'Bearer {}'.format(token)}, params=payload)
    return response.json()


def personality_insights(username):
    tweets = timeline(username)
    content_items = {}
    content_items['contentItems'] = []

    for tweet in tweets:
        item = {
            'id': 'TW'+str(tweet['id']),
            'content': tweet['text'],
            'contenttype': 'text/plain',
            'created': parser.parse(tweet['created_at']).timestamp(),
            'forward': tweet['retweeted'], 
            'reply': bool(tweet['in_reply_to_screen_name']),
        }
        content_items['contentItems'].append(item)

    with open('creds.yaml') as file:
        creds = yaml.load(file)

    insights = PersonalityInsightsV3(
        version='2016-10-20',
        username=creds['IBM']['ServiceUsername'],
        password=creds['IBM']['ServicePassword'])

    profile = insights.profile(content_items, content_type='application/json', raw_scores=False, consumption_preferences=True)
    return json.dumps(profile, indent=2)



print(personality_insights('SkullTech101'))
