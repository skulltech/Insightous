import twitter
import facebook



def twitter(key, secret):
    api = twitter.Api(consumer_key='urnMiSi6fhCKIGlSxGA9JVVp0',
                      consumer_secret='IAY8FJknVRouNvFdlSFEMBAgvAlGygbpyp8SSAlFDYvRkszDZq',
                      access_token_key=key,
                      access_token_secret=secret)
    tweets = api.GetHomeTimeline()
    return [tweet.text for tweet in tweets]


def facebook(token):
    graph = facebook.GraphAPI(access_token=token)
