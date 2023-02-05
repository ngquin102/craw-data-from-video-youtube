# -*- coding: utf-8 -*-
"""crawdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17qwY3X_Q7Jgei8tCOOcG6LUP86xHugEd
"""

import requests

api_key = "YOUR_API_KEY"
video_id = "video_id"

url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

response = requests.get(url)
data = response.json()

# Get the title and description of the video
video_title = data["items"][0]["snippet"]["title"]
video_description = data["items"][0]["snippet"]["description"]

print("Video Title:", video_title)
print("Video Description:", video_description)