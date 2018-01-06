import twitter
import facebook
import yaml
from requests_oauthlib import OAuth1Session
import webbrowser



REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'


def tweets(username):
    with open('creds.yaml') as file:
        creds = yaml.load(file)

    token = get_access_token(creds['Twitter']['ConsumerKey'], creds['Twitter']['ConsumerSecret'])
    api = twitter.Api(consumer_key=creds['Twitter']['ConsumerKey'],
                      consumer_secret=creds['Twitter']['ConsumerSecret'],
                      access_token_key=token['atk'],
                      access_token_secret=token['ats'])
    tweets = api.GetUserTimeline(screen_name=username)
    return tweets


def get_access_token(consumer_key, consumer_secret):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')

    print('\nRequesting temp token from Twitter...\n')

    try:
        resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    except ValueError as e:
        raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

    url = oauth_client.authorization_url(AUTHORIZATION_URL)

    print('I will try to start a browser to visit the following Twitter page '
          'if a browser will not start, copy the URL to your browser '
          'and retrieve the pincode to be used '
          'in the next step to obtaining an Authentication Token: \n'
          '\n\t{0}'.format(url))

    webbrowser.open(url)
    pincode = input('\nEnter your pincode? ')

    print('\nGenerating and signing request for an access token...\n')

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                 resource_owner_key=resp.get('oauth_token'),
                                 resource_owner_secret=resp.get('oauth_token_secret'),
                                 verifier=pincode)
    try:
        resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError as e:
        raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

    print('Succesfully retrieved OAuth access token. Thank you!')
    return {'atk': resp.get('oauth_token'), 'ats': resp.get('oauth_token_secret')}


def main():
    print(tweets('SkullTech101'))



if __name__=='__main__':
    main()
