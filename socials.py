import twitter
import facebook
import requests


def twitter(key, secret, username):
    api = twitter.Api(consumer_key='urnMiSi6fhCKIGlSxGA9JVVp0',
                      consumer_secret='IAY8FJknVRouNvFdlSFEMBAgvAlGygbpyp8SSAlFDYvRkszDZq',
                      access_token_key=key,
                      access_token_secret=secret)
    tweets = api.GetUserTimeline(screen_name=username)
    return tweets

def facebook(access_token, user_id)

	graph = facebook.GraphAPI(access_token)
	profile = graph.get_object(user_id)
	posts = graph.get_connections(profile['id'], 'posts')

	while True:
	    try:
	        [print(post['message']) for post in posts['data']]
	        posts = requests.get(posts['paging']['next']).json()
	    except KeyError:
	        break