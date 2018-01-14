
import json
import requests

#set up variables
CLIENT_ID = "p-jcoLKBynTLew"
CLIENT_SECRET = "gko_LXELoV07ZBNUXrvWZfzE3aI"
REDIRECT_URI = "http://localhost:65010/reddit_callback"


#send the data to Dynamics CRM Server
api_token = 'your_api_token'
api_url_base = 'https://api.digitalocean.com/v2/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}