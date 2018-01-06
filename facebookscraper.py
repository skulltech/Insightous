import facebook
import requests
import json

def get_fb_token(app_id, app_secret):           
    
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    
    data = file.json()
    print(data)
    access_token = data['access_token']

    return (access_token)



def facebookscraper(access_token, user_id):

	graph = facebook.GraphAPI(access_token)
	profile = graph.get_object(user_id)
	posts = graph.get_connections(profile['id'], 'posts')

	while True:
	    try:
	        [print(post['message']) for post in posts['data']]
	        posts = requests.get(posts['paging']['next']).json()
	    except KeyError:
	        break



if __name__=="__main__":
	s=get_fb_token(app_id, app_secret)
	facebookscraper(s,"me")