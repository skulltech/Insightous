import json
import yaml
import base64
import requests
from dateutil import parser
from urllib.parse import quote_plus
from watson_developer_cloud import PersonalityInsightsV3



def get_token():
    with open('creds.yaml') as file:
        creds = yaml.load(file)

    credentials = quote_plus(creds['Twitter']['ConsumerKey']) + ':' + quote_plus(creds['Twitter']['ConsumerSecret'])
    credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        'Authorization': 'Basic {}'.format(credentials),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'User-Agent': 'CodeFunDo-VAS App'
    }
    response = requests.post('https://api.twitter.com/oauth2/token', headers=headers, data={'grant_type': 'client_credentials'})
    return response.json()['access_token']


def timeline(username, token=None):
    token = token or get_token()
    payload = {
        'screen_name': username,
        'include_rts': True,
    }
    response = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json', 
                            headers={'Authorization': 'Bearer {}'.format(token)}, params=payload)
    return response.json()


def personality_insights(username, token=None):
    tweets = timeline(username, token)
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
    return profile


def main():
    username = input('[*] Enter the Twitter screen name: ')
    profile = personality_insights(username)
    print(json.dumps(profile, indent=2))


if __name__='__main__':
    main()
