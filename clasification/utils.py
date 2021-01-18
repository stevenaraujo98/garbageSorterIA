import requests
import json

ClienID = "3f7ed01fe5374d9"
ClientSecret = "878e8fd1f0c170cf2691f254ca7519bfac9fac39"

def submit_image(image_file):
    if image_file != None:
        url = "https://api.imgur.com/3/image"
        payload = {"image": image_file.read()}
        headers = {"Authorization": "Client-ID " + ClienID}

        res = requests.post(url, headers=headers, data=payload)
        if res.status_code >= 300:
            return None
        elif res.status_code >= 200:
            return res.json()["data"]["link"]
    return None

def submit_results(clase, img, accuracy):
    url = "https://clasification-0871.restdb.io/rest/images"

    payload = json.dumps( {"class": clase, "img": img, "accuracy": accuracy} )
    headers = {
        'content-type': "application/json",
        'x-apikey': "6004c9251346a1524ff12b8a",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()