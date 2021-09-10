import random
import os
import requests
from googleapiclient.discovery import build
import time as t
import dotenv

dotenv.load_dotenv()

isapi_key = os.environ['API_KEY']


def search(search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=isapi_key).cse()
    result = resource.list(
        q=f"{search}", cx="54c1117c3e104029b", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    print(url)

    response = requests.get(url, stream=True)

    with open('image.jpg','wb') as f:
        f.write(response.content)
        f.close()

input = input('What would you like to search for? ')
search(input)

t.sleep(5)
os.remove('image.jpg')
