import requests
import ctypes
import os

# constants and params
SPI_SETDESKWALLPAPER = 20
DIRNAME = "garfieldbot5001"
FILENAME = 'garf.jpg'
USER = "GarfieldBot5000"
TOKEN = "twitter api v2 token" ### REPLACE WITH YOUR PERSONAL TOKEN ###

# saves user's latest tweet with an image to path
def recent_tweet_image(user, token, path):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f"https://api.twitter.com/2/users/by/username/{user}"
    id = requests.request("GET", url, headers=headers).json()["data"]["id"]
    url = f"https://api.twitter.com/2/users/{id}/tweets"
    resp = requests.request("GET", url, headers=headers)
    for tweet in resp.json()["data"]:
        tweet_id = tweet["id"]
        url = f"https://api.twitter.com/2/tweets/{tweet_id}?expansions=attachments.media_keys&media.fields=url"
        resp = requests.request("GET", url, headers=headers)
        resp = resp.json()
        if "includes" in resp and \
            "media" in resp["includes"] and \
            resp["includes"]["media"][0]["type"] == "photo":
            url = resp["includes"]["media"][0]["url"]
            resp = requests.request("GET", url, headers=headers)
            with open(path,'wb') as f:
                f.write(resp.content)
            return
    raise Exception("No tweet with image found")

if __name__ == "__main__":
    path = os.path.join(os.path.expanduser("~"), DIRNAME)
    try:
        os.mkdir(path)
    except:
        pass
    path = os.path.join(path,FILENAME)
    recent_tweet_image(USER,TOKEN, path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    