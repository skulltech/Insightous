import facebook
import requests



def facebook(access_token, user_id):

	graph = facebook.GraphAPI(access_token)
	profile = graph.get_object(user_id)
	posts = graph.get_connections(profile['id'], 'posts')

	while True:
	    try:
	        [print(post['message']) for post in posts['data']]
	        posts = requests.get(posts['paging']['next']).json()
	    except KeyError:
	        break
