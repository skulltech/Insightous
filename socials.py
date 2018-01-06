import twitter
import facebook



def twitter(key, secret, username):
    api = twitter.Api(consumer_key='urnMiSi6fhCKIGlSxGA9JVVp0',
                      consumer_secret='IAY8FJknVRouNvFdlSFEMBAgvAlGygbpyp8SSAlFDYvRkszDZq',
                      access_token_key=key,
                      access_token_secret=secret)
    tweets = api.GetUserTimeline(screen_name=username)
    return tweets
