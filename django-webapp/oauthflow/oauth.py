import requests
import yaml
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


print(bearer_token())