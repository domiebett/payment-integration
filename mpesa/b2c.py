import requests
import json

from mpesa.authenticate import authenticate

def b2c():
    access_token = json.loads(authenticate())["access_token"]
    api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    headers = { "Authorization" : "Bearer {}".format(access_token) }
    request = {
        "InitiatorName": "apiop7",
        "SecurityCredential":"G9NpKPCB",
        "CommandID": "BusinessPayment",
        "Amount": "3000",
        "PartyA": "603082",
        "PartyB": "254708374149",
        "Remarks": "Hopefully I just successfully managed to change this.",
        "QueueTimeOutURL": "http://stackoverflow.com",
        "ResultURL": "http://google.com",
        "Occasion": " "
    }

    response = requests.post(api_url, json = request, headers = headers)
    return response.text