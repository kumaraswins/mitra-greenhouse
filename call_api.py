import requests


def get_person_details(email, token):
    url = "https://harvest.greenhouse.io/v1/candidates/?email={}".format(email)
    headers = {
    'Authorization': 'Basic {}'.format(token)
    }
    response = requests.request("GET", url, headers=headers, data={})
    return (response.text)
