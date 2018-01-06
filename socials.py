import twitter
import facebook
import yaml



def twitter(key, secret, username):
    with open('creds.yaml') as file:
        creds = yaml.load(file)

    api = twitter.Api(consumer_key=creds['Twitter']['ConsumerKey'],
                      consumer_secret=creds['Twitter']['ConsumerSecret'],
                      access_token_key=key,
                      access_token_secret=secret)
    tweets = api.GetUserTimeline(screen_name=username)
    return tweets
