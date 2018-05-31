import requests
from requests.auth import HTTPBasicAuth


def authenticate():
    consumerKey = "EmwojzdPx7NwTPsSWhGI55j4MfUSxuJN"
    consumerSecret = "AzIu9a3X3SdGAOXB"
    apiUrl = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(apiUrl, auth=HTTPBasicAuth(consumerKey, consumerSecret))

    print(response.text)
    return response.text
