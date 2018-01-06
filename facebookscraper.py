import facebook
import requests
import json

def get_fb_token(app_id, app_secret):           
    """returns app access token, using @param : app_id and app_secret"""
    
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    
    data = file.json()
    app_access_token = data['access_token']

    return (app_access_token)



def facebookscraper(user_access_token, user_id="me"):
	"""it takes user access token and retrive the posts"""
	
	graph = facebook.GraphAPI(access_token)
	
	profile = graph.get_object(user_id)
	posts = graph.get_connections(profile['id'], 'posts')

	while True:
	    
	    try:
	        [print(post['message']) for post in posts['data']]
	        posts = requests.get(posts['paging']['next']).json()
	    except KeyError:
	        break
