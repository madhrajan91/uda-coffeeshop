import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen





AUTH0_DOMAIN = 'udacity-fsnd.auth0.com' #dev-identityaccess.auth0.com
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'


AUTH0_AUTHORIZE_URL="https://dev-identityaccess.auth0.com/authorize?client_id=ojMkR23sKilvgIJcnk949eK9sPjZzQc4&audience=coffee&response_type=token&redirect_uri=http://localhost:5000/login-results"
# Manager access token:
'http://localhost:5000/login-results#access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5UbEROekV4UmpVNE9USXpSalk1TmtFMk0wUTNORFZFUWpoRlFUaERORFl3TkRZM05UazROUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1pZGVudGl0eWFjY2Vzcy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRiZGYwMmIxMmI1YmIwZTI2MGVjM2IxIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNTcyNzI5MjM3LCJleHAiOjE1NzI3MzY0MzcsImF6cCI6Im9qTWtSMjNzS2lsdmdJSmNuazk0OWVLOXNQalp6UWM0Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.n27y-h5kYB-qj9igpmzeRs1SkAUCTiYt9paVw74lOvnZ4PXoN7RwoNe4PY0wLsn0GbHzSudrpSHlWEiGj1CH05QnHSP05TeMFghp-slt2EzEOmZ4935Rz-NUzDeWBrCTCRKnZ_ygKKlbKAuBZkr1a5eFR-qu0VYOGbYn5xNvwCs7rni0ztrjdLg41fl4eqLBXLfGID_gbc6ddHVRCkKSCO_WVeWk2ZzYp3mhp89fPFTnVl0ZD4zpUFMfB2g0oHPNiO2PRHly7wgyenMNpHRw_XrgAsykdKrDP7hhPMzUXZLHuiR3BodqAgZRP-4vi1PNhoD7KOP6p6F0wWulp1QvHQ&expires_in=7200&token_type=Bearer'
## AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header

'''
@TODO implement get_token_auth_header() method
    it should attempt to get the header from the request
        it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
        it should raise an AuthError if the header is malformed
    return the token part of the header
'''
def get_token_auth_header():
   raise Exception('Not Implemented')

'''
@TODO implement check_permissions(permission, payload) method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission string is not in the payload permissions array
    return true otherwise
'''
def check_permissions(permission, payload):
    raise Exception('Not Implemented')

'''
@TODO implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload

    !!NOTE urlopen has a common certificate error described here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
'''
def verify_decode_jwt(token):
    raise Exception('Not Implemented')

'''
@TODO implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
'''
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator