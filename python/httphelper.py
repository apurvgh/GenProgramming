
import json
import requests

#Sample extracted from Stack overflow https://stackoverflow.com/questions/36719540/how-can-i-get-an-oauth2-access-token-using-python

class ExampleOAuth2Client:
    def __init__(self, client_id, client_secret):
        self.access_token = None
        self.service = OAuth2Service(
            name="foo",
            client_id=client_id,
            client_secret=client_secret,
            access_token_url="http://api.example.com/oauth/access_token",
            authorize_url="http://api.example.com/oauth/access_token",
            base_url="http://api.example.com/",
        )

        self.get_access_token()

    def get_access_token(self):
        data = {'code': 'bar',
                'grant_type': 'client_credentials',
                'redirect_uri': 'http://example.com/'}

        session = self.service.get_auth_session(data=data, decoder=json.loads)

        self.access_token = session.access_token